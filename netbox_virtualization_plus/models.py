from django.db import models
from django.core.exceptions import ValidationError
from netbox.models import NetBoxModel
from ipam.models import (
    VLAN,
)
from dcim.models import (
    Device,
    Interface
)
from virtualization.models import (
    Cluster,
    VirtualMachine,
    VMInterface,
    VirtualDisk,  
)

class VMSnapshot(NetBoxModel):
    """
    Represents a snapshot of a VirtualMachine, potentially including memory
    or other snapshot details.
    """
    name = models.CharField(max_length=100)
    virtual_machine = models.ForeignKey(
        to=VirtualMachine,
        on_delete=models.CASCADE,
        related_name='snapshots'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    size_gb = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Size consumed by this snapshot"
    )
    memory_included = models.BooleanField(
        default=False,
        help_text="Whether the VM memory state is also captured"
    )
    snapshot_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="Full, Incremental, Quiesced, etc."
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.virtual_machine.name} - {self.name}"

class Datastore(NetBoxModel):
    """
    Represents a storage unit for your virtualization clusters (NFS, iSCSI, etc.).
    A cluster can have multiple datastores. 
    """
    name = models.CharField(max_length=100, unique=True)

    # Either cluster or device must be set, not both
    cluster = models.ForeignKey(
        to=Cluster,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='datastores'
    )
    host = models.ForeignKey(
        to=Device,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='datastores'
    )
    capacity_gb = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text="Total capacity"
    )
    used_gb = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text="Used capacity"
    )
    datastore_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. Local, iSCSI, FC, NFS, CIFS/SMB"
    )
    storage_device = models.ForeignKey(
        to=Device,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='datastore_attachments',
        help_text="The storage device (SAN, NAS, etc.)"
    )
    mount_point = models.CharField(
        max_length=255,
        blank=True,
        help_text="NFS Share, ISCSI/FC LUN, SMB Share, etc"
    )

    description = models.TextField(blank=True)

    def clean(self):
        # Ensure exactly one of (cluster, device) is set
        if not self.cluster and not self.host:
            raise ValidationError("You must specify either a cluster or a host for this datastore.")
        if self.cluster and self.host:
            raise ValidationError("You cannot specify both a cluster and a host on the same datastore.")

    def __str__(self):
        # Show which side is attached
        if self.cluster:
            return f"{self.name} (attached to cluster: {self.cluster.name})"
        else:
            return f"{self.name} (attached to host: {self.host.name})"

#
# Extension of NetBox's VirtualDisk to link it with a plugin Datastore
#
class VirtualDiskExtension(NetBoxModel):
    """
    1-to-1 extension of the built-in VirtualDisk. We reference the plugin's Datastore.
    This avoids altering the NetBox core 'virtualization_virtualdisk' table.
    """
    virtual_disk = models.OneToOneField(
        to=VirtualDisk,
        on_delete=models.CASCADE,
        related_name='plugin_extension',
        help_text="Reference to the built-in NetBox VirtualDisk"
    )
    datastore = models.ForeignKey(
        to=Datastore,
        on_delete=models.PROTECT,
        related_name='virtual_disks',
        help_text="Which datastore this disk is on"
    )
    # Additional fields as needed, e.g. replication group, backup ID, etc.
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Extension for {self.virtual_disk}"


#
# Virtual Switch (generic)
#
class VirtualSwitch(NetBoxModel):
    """
    Represents a hypervisor-level switch (VMware, Hyper-V, Proxmox Bridge, etc.).
    """
    name = models.CharField(max_length=100, unique=True)
    cluster = models.ForeignKey(
        to=Cluster,
        on_delete=models.PROTECT,
        related_name='virtual_switches'
    )
    switch_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. Standard, Distributed, Open vSwitch, etc."
    )
    version = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. vDS 7.0, OVS 2.15, etc."
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


#
# Virtual Network (generalized PortGroup)
#
class VirtualNetwork(NetBoxModel):
    """
    General abstraction of a port group, network bridge, or vSwitch network.
    """
    name = models.CharField(max_length=100)
    virtual_switch = models.ForeignKey(
        to=VirtualSwitch,
        on_delete=models.PROTECT,
        related_name='virtual_networks'
    )
    trunk_allowed_vlans = models.CharField(
        max_length=200,
        blank=True,
        help_text="Comma/hyphen separated if trunking multiple VLANs (e.g. '10,11-20')"
    )
    network_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. Static, Ephemeral, Proxmox bridge, etc."
    )
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('virtual_switch', 'name')

    def __str__(self):
        return f"{self.virtual_switch.name} - {self.name}"

#
# Switch Uplink
#
class VirtualSwitchUplink(NetBoxModel):
    """
    Represents the link from the VirtualSwitch to the physical NIC (dcim.Interface) on the host.
    """
    name = models.CharField(max_length=100, blank=True)
    virtual_switch = models.ForeignKey(
        to=VirtualSwitch,
        on_delete=models.CASCADE,
        related_name='uplinks'
    )
    interface = models.ForeignKey(
        to=Interface,
        on_delete=models.CASCADE,
        related_name='virtual_switch_uplinks'
    )
    lacp_enabled = models.BooleanField(default=False)
    teaming_policy = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g. active-active, active-standby, etc."
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name or f"Uplink to {self.interface.name}"


#
# VMInterface Extension for linking NetBox VMInterface to a plugin VirtualNetwork
#
class VMInterfaceExtension(NetBoxModel):
    """
    Since we can't add columns directly to virtualization_vminterface safely,
    we create a 1-to-1 extension that references a plugin VirtualNetwork.
    """
    vm_interface = models.OneToOneField(
        to=VMInterface,
        on_delete=models.CASCADE,
        related_name='plugin_extension',
        help_text="The existing VM Interface from NetBox"
    )
    vlan = models.ForeignKey(
        to=VLAN,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="802.1Q VLAN ID"
    )
    virtual_network = models.ForeignKey(
        to=VirtualNetwork,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Which VirtualNetwork (portgroup/bridge) this interface connects to"
    )
    # Additional fields if needed: port security, QoS policy, etc.
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Extension for {self.vm_interface.name}"


class ResourcePool(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    cluster = models.ForeignKey(
        to=Cluster,
        on_delete=models.PROTECT,
        related_name='resource_pools'
    )
    pool_type = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ResourceScheduling(NetBoxModel):
    cluster = models.OneToOneField(
        to=Cluster,
        on_delete=models.CASCADE,
        related_name='resource_scheduling'
    )
    enabled = models.BooleanField(default=False)
    automation_level = models.CharField(max_length=50, blank=True)
    imbalance_threshold = models.IntegerField(default=5)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Resource Scheduling for {self.cluster.name}"


class HighAvailability(NetBoxModel):
    cluster = models.OneToOneField(
        to=Cluster,
        on_delete=models.CASCADE,
        related_name='high_availability'
    )
    enabled = models.BooleanField(default=False)
    failover_level = models.PositiveIntegerField(default=1)
    admission_control_enabled = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"High Availability for {self.cluster.name}"
