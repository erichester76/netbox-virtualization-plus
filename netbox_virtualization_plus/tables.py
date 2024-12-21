from netbox.tables import NetBoxTable
from django_tables2 import columns
import netbox_virtualization_plus.models as models

class VMSnapshotTable(NetBoxTable):
    name = columns.Column(linkify=True)
    virtual_machine = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.VMSnapshot
        fields = (
            'pk',
            'id',
            'name',
            'virtual_machine',
            'created_at',
            'size_gb',
            'memory_included',
            'snapshot_type',
            'description',
        )
        default_columns = ('name', 'virtual_machine', 'created_at')

#
# Datastore
#
class DatastoreTable(NetBoxTable):
    name = columns.Column(linkify=True)
    cluster = columns.Column(linkify=True)
    host = columns.Column(linkify=True)
    storage_device = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.Datastore
        fields = (
            'pk', 'id', 'name', 'cluster', 'host', 'capacity_gb',
            'used_gb', 'datastore_type', 'storage_device', 'mount_point', 'description'
        )
        default_columns = ('name', 'cluster', 'host', 'capacity_gb', 'used_gb')


#
# VirtualDiskExtension
#
class VirtualDiskExtensionTable(NetBoxTable):
    virtual_disk = columns.Column(linkify=True)
    datastore = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.VirtualDiskExtension
        fields = (
            'pk', 'id', 'virtual_disk', 'datastore', 'notes'
        )
        default_columns = ('virtual_disk', 'datastore')


#
# VirtualSwitch
#
class VirtualSwitchTable(NetBoxTable):
    name = columns.Column(linkify=True)
    cluster = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.VirtualSwitch
        fields = (
            'pk', 'id', 'name', 'cluster', 'switch_type', 'version', 'description'
        )
        default_columns = ('name', 'cluster', 'switch_type', 'version')


#
# VirtualNetwork
#
class VirtualNetworkTable(NetBoxTable):
    name = columns.Column(linkify=True)
    virtual_switch = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.VirtualNetwork
        fields = (
            'pk', 'id', 'name', 'virtual_switch', 'trunk_allowed_vlans',
            'network_type', 'description'
        )
        default_columns = ('name', 'virtual_switch')


#
# VirtualSwitchUplink
#
class VirtualSwitchUplinkTable(NetBoxTable):
    name = columns.Column(linkify=True)
    virtual_switch = columns.Column(linkify=True)
    interface = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.VirtualSwitchUplink
        fields = (
            'pk', 'id', 'name', 'virtual_switch', 'interface',
            'lacp_enabled', 'teaming_policy', 'description'
        )
        default_columns = ('name', 'virtual_switch', 'interface')


#
# VMInterfaceExtension
#
class VMInterfaceExtensionTable(NetBoxTable):
    vm_interface = columns.Column(linkify=True)
    vlan_id = columns.Column(linkify=True)
    virtual_network = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.VMInterfaceExtension
        fields = (
            'pk', 'id', 'vm_interface', 'vlan', 'virtual_network', 'notes'
        )
        default_columns = ('vm_interface', 'vlan', 'virtual_network')


#
# ResourcePool
#
class ResourcePoolTable(NetBoxTable):
    name = columns.Column(linkify=True)
    cluster = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.ResourcePool
        fields = (
            'pk', 'id', 'name', 'cluster', 'pool_type', 'description'
        )
        default_columns = ('name', 'cluster', 'pool_type')


#
# ResourceScheduling
#
class ResourceSchedulingTable(NetBoxTable):
    cluster = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.ResourceScheduling
        fields = (
            'pk', 'id', 'cluster', 'enabled',
            'automation_level', 'imbalance_threshold', 'description'
        )
        default_columns = ('cluster', 'enabled', 'automation_level')


#
# HighAvailability
#
class HighAvailabilityTable(NetBoxTable):
    cluster = columns.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = models.HighAvailability
        fields = (
            'pk', 'id', 'cluster', 'enabled', 'failover_level',
            'admission_control_enabled', 'description'
        )
        default_columns = ('cluster', 'enabled', 'failover_level')
