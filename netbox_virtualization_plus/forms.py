from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm, NetBoxModelImportForm
import netbox_virtualization_plus.models as models
from ipam.models import VLAN

#
# VMSnapshot
#
class VMSnapshotForm(NetBoxModelForm):
    class Meta:
        model = models.VMSnapshot
        fields = (
            'name',
            'virtual_machine',
            'size_gb',
            'memory_included',
            'snapshot_type',
            'description',
        )


class VMSnapshotBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VMSnapshot.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    memory_included = forms.NullBooleanField(required=False)

    class Meta:
        nullable_fields = ['description', 'snapshot_type']


class VMSnapshotImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.VMSnapshot
        fields = (
            'name',
            'virtual_machine',
            'size_gb',
            'memory_included',
            'snapshot_type',
            'description',
        )

#
# Datastore
#
class DatastoreForm(NetBoxModelForm):
    class Meta:
        model = models.Datastore
        fields = (
            'name', 'cluster', 'host', 'capacity_gb', 'used_gb',
            'datastore_type', 'storage_device', 'mount_point', 'description'
        )


class DatastoreBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.Datastore.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    cluster = forms.ModelChoiceField(
        queryset=models.Cluster.objects.all(),
        required=False
    )
    host = forms.ModelChoiceField(
        queryset=models.Device.objects.all(),
        required=False
    )

    class Meta:
        nullable_fields = ['mount_point', 'storage_device', 'description']


class DatastoreImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.Datastore
        fields = (
            'name', 'cluster', 'host', 'capacity_gb', 'used_gb',
            'datastore_type', 'storage_device', 'mount_point', 'description'
        )


#
# VirtualDiskExtension
#
class VirtualDiskExtensionForm(NetBoxModelForm):
    class Meta:
        model = models.VirtualDiskExtension
        fields = ('virtual_disk', 'datastore', 'notes')


class VirtualDiskExtensionBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VirtualDiskExtension.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    datastore = forms.ModelChoiceField(
        queryset=models.Datastore.objects.all(),
        required=False
    )

    class Meta:
        nullable_fields = ['notes']


class VirtualDiskExtensionImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.VirtualDiskExtension
        fields = ('virtual_disk', 'datastore', 'notes')


#
# VirtualSwitch
#
class VirtualSwitchForm(NetBoxModelForm):
    class Meta:
        model = models.VirtualSwitch
        fields = ('name', 'cluster', 'switch_type', 'version', 'description')


class VirtualSwitchBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VirtualSwitch.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    cluster = forms.ModelChoiceField(
        queryset=models.Cluster.objects.all(),
        required=False
    )

    class Meta:
        nullable_fields = ['switch_type', 'version', 'description']


class VirtualSwitchImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.VirtualSwitch
        fields = ('name', 'cluster', 'switch_type', 'version', 'description')


#
# VirtualNetwork
#
class VirtualNetworkForm(NetBoxModelForm):
    class Meta:
        model = models.VirtualNetwork
        fields = (
            'name', 'virtual_switch', 'trunk_allowed_vlans',
            'network_type', 'description'
        )


class VirtualNetworkBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VirtualNetwork.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    virtual_switch = forms.ModelChoiceField(
        queryset=models.VirtualSwitch.objects.all(),
        required=False
    )

    class Meta:
        nullable_fields = ['trunk_allowed_vlans', 'network_type', 'description']


class VirtualNetworkImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.VirtualNetwork
        fields = (
            'name', 'virtual_switch', 'trunk_allowed_vlans',
            'network_type', 'description'
        )


#
# VirtualSwitchUplink
#
class VirtualSwitchUplinkForm(NetBoxModelForm):
    class Meta:
        model = models.VirtualSwitchUplink
        fields = (
            'name', 'virtual_switch', 'interface',
            'lacp_enabled', 'teaming_policy', 'description'
        )


class VirtualSwitchUplinkBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VirtualSwitchUplink.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    virtual_switch = forms.ModelChoiceField(
        queryset=models.VirtualSwitch.objects.all(),
        required=False
    )

    class Meta:
        nullable_fields = ['description', 'teaming_policy']


class VirtualSwitchUplinkImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.VirtualSwitchUplink
        fields = (
            'name', 'virtual_switch', 'interface',
            'lacp_enabled', 'teaming_policy', 'description'
        )


#
# VMInterfaceExtension
#
class VMInterfaceExtensionForm(NetBoxModelForm):
    class Meta:
        model = models.VMInterfaceExtension
        fields = ('vm_interface', 'vlan', 'virtual_network', 'notes')


class VMInterfaceExtensionBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VMInterfaceExtension.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    vlan = forms.ModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False
    )
    virtual_network = forms.ModelChoiceField(
        queryset=models.VirtualNetwork.objects.all(),
        required=False
    )

    class Meta:
        nullable_fields = ['notes']


class VMInterfaceExtensionImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.VMInterfaceExtension
        fields = ('vm_interface', 'vlan', 'virtual_network', 'notes')


#
# ResourcePool
#
class ResourcePoolForm(NetBoxModelForm):
    class Meta:
        model = models.ResourcePool
        fields = ('name', 'cluster', 'pool_type', 'description')


class ResourcePoolBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.ResourcePool.objects.all(),
        widget=forms.MultipleHiddenInput()
    )

    class Meta:
        nullable_fields = ['pool_type', 'description']


class ResourcePoolImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.ResourcePool
        fields = ('name', 'cluster', 'pool_type', 'description')


#
# ResourceScheduling
#
class ResourceSchedulingForm(NetBoxModelForm):
    class Meta:
        model = models.ResourceScheduling
        fields = (
            'cluster', 'enabled', 'automation_level',
            'imbalance_threshold', 'description'
        )


class ResourceSchedulingBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.ResourceScheduling.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    enabled = forms.NullBooleanField(required=False)

    class Meta:
        nullable_fields = ['description']


class ResourceSchedulingImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.ResourceScheduling
        fields = (
            'cluster', 'enabled', 'automation_level',
            'imbalance_threshold', 'description'
        )


#
# HighAvailability
#
class HighAvailabilityForm(NetBoxModelForm):
    class Meta:
        model = models.HighAvailability
        fields = (
            'cluster', 'enabled', 'failover_level',
            'admission_control_enabled', 'description'
        )


class HighAvailabilityBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.HighAvailability.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    enabled = forms.NullBooleanField(required=False)

    class Meta:
        nullable_fields = ['description']


class HighAvailabilityImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.HighAvailability
        fields = (
            'cluster', 'enabled', 'failover_level',
            'admission_control_enabled', 'description'
        )
