from django import forms
from utilities.forms import NetBoxModelForm, BulkEditForm, CSVModelForm
import virtualization_plus.models as models

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


class VMSnapshotBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VMSnapshot.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    memory_included = forms.NullBooleanField(required=False)

    class Meta:
        nullable_fields = ['description', 'snapshot_type']


class VMSnapshotImportForm(CSVModelForm):
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


class DatastoreBulkEditForm(BulkEditForm):
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


class DatastoreImportForm(CSVModelForm):
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


class VirtualDiskExtensionBulkEditForm(BulkEditForm):
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


class VirtualDiskExtensionImportForm(CSVModelForm):
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


class VirtualSwitchBulkEditForm(BulkEditForm):
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


class VirtualSwitchImportForm(CSVModelForm):
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


class VirtualNetworkBulkEditForm(BulkEditForm):
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


class VirtualNetworkImportForm(CSVModelForm):
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


class VirtualSwitchUplinkBulkEditForm(BulkEditForm):
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


class VirtualSwitchUplinkImportForm(CSVModelForm):
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
        fields = ('vm_interface', 'vlan_id', 'virtual_network', 'notes')


class VMInterfaceExtensionBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.VMInterfaceExtension.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    vlan_id = forms.ModelChoiceField(
        queryset=models.Vlan.objects.all(),
        required=False
    )
    virtual_network = forms.ModelChoiceField(
        queryset=models.VirtualNetwork.objects.all(),
        required=False
    )

    class Meta:
        nullable_fields = ['notes']


class VMInterfaceExtensionImportForm(CSVModelForm):
    class Meta:
        model = models.VMInterfaceExtension
        fields = ('vm_interface', 'vlan_id', 'virtual_network', 'notes')


#
# ResourcePool
#
class ResourcePoolForm(NetBoxModelForm):
    class Meta:
        model = models.ResourcePool
        fields = ('name', 'cluster', 'pool_type', 'description')


class ResourcePoolBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.ResourcePool.objects.all(),
        widget=forms.MultipleHiddenInput()
    )

    class Meta:
        nullable_fields = ['pool_type', 'description']


class ResourcePoolImportForm(CSVModelForm):
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


class ResourceSchedulingBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.ResourceScheduling.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    enabled = forms.NullBooleanField(required=False)

    class Meta:
        nullable_fields = ['description']


class ResourceSchedulingImportForm(CSVModelForm):
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


class HighAvailabilityBulkEditForm(BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=models.HighAvailability.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    enabled = forms.NullBooleanField(required=False)

    class Meta:
        nullable_fields = ['description']


class HighAvailabilityImportForm(CSVModelForm):
    class Meta:
        model = models.HighAvailability
        fields = (
            'cluster', 'enabled', 'failover_level',
            'admission_control_enabled', 'description'
        )
