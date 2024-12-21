from netbox.views import generic
import netbox_virtualization_plus.models as models
import netbox_virtualization_plus.forms as forms
import netbox_virtualization_plus.filtersets as filtersets
import netbox_virtualization_plus.tables as tables


#
# VMSnapshot
#
class VMSnapshotListView(generic.ObjectListView):
    queryset = models.VMSnapshot.objects.all()
    filterset = filtersets.VMSnapshotFilterSet
    table = tables.VMSnapshotTable

class VMSnapshotView(generic.ObjectView):
    queryset = models.VMSnapshot.objects.all()

class VMSnapshotEditView(generic.ObjectEditView):
    queryset = models.VMSnapshot.objects.all()
    form = forms.VMSnapshotForm

class VMSnapshotDeleteView(generic.ObjectDeleteView):
    queryset = models.VMSnapshot.objects.all()

class VMSnapshotBulkEditView(generic.BulkEditView):
    queryset = models.VMSnapshot.objects.all()
    filterset = filtersets.VMSnapshotFilterSet
    table = tables.VMSnapshotTable
    form = forms.VMSnapshotBulkEditForm

class VMSnapshotBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VMSnapshot.objects.all()
    filterset = filtersets.VMSnapshotFilterSet
    table = tables.VMSnapshotTable

class VMSnapshotImportView(generic.BulkImportView):
    queryset = models.VMSnapshot.objects.all()
    model_form = forms.VMSnapshotImportForm

class VMSnapshotChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VMSnapshot.objects.all()


#
# Datastore
#
class DatastoreListView(generic.ObjectListView):
    queryset = models.Datastore.objects.all()
    filterset = filtersets.DatastoreFilterSet
    table = tables.DatastoreTable

class DatastoreView(generic.ObjectView):
    queryset = models.Datastore.objects.all()

class DatastoreEditView(generic.ObjectEditView):
    queryset = models.Datastore.objects.all()
    form = forms.DatastoreForm

class DatastoreDeleteView(generic.ObjectDeleteView):
    queryset = models.Datastore.objects.all()

class DatastoreBulkEditView(generic.BulkEditView):
    queryset = models.Datastore.objects.all()
    filterset = filtersets.DatastoreFilterSet
    table = tables.DatastoreTable
    form = forms.DatastoreBulkEditForm

class DatastoreBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Datastore.objects.all()
    filterset = filtersets.DatastoreFilterSet
    table = tables.DatastoreTable

class DatastoreImportView(generic.BulkImportView):
    queryset = models.Datastore.objects.all()
    model_form = forms.DatastoreImportForm

class DatastoreChangeLogView(generic.ObjectChangeLogView):
    queryset = models.Datastore.objects.all()


#
# VirtualDiskExtension
#
class VirtualDiskExtensionListView(generic.ObjectListView):
    queryset = models.VirtualDiskExtension.objects.all()
    filterset = filtersets.VirtualDiskExtensionFilterSet
    table = tables.VirtualDiskExtensionTable

class VirtualDiskExtensionView(generic.ObjectView):
    queryset = models.VirtualDiskExtension.objects.all()

class VirtualDiskExtensionEditView(generic.ObjectEditView):
    queryset = models.VirtualDiskExtension.objects.all()
    form = forms.VirtualDiskExtensionForm

class VirtualDiskExtensionDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualDiskExtension.objects.all()

class VirtualDiskExtensionBulkEditView(generic.BulkEditView):
    queryset = models.VirtualDiskExtension.objects.all()
    filterset = filtersets.VirtualDiskExtensionFilterSet
    table = tables.VirtualDiskExtensionTable
    form = forms.VirtualDiskExtensionBulkEditForm

class VirtualDiskExtensionBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VirtualDiskExtension.objects.all()
    filterset = filtersets.VirtualDiskExtensionFilterSet
    table = tables.VirtualDiskExtensionTable

class VirtualDiskExtensionImportView(generic.BulkImportView):
    queryset = models.VirtualDiskExtension.objects.all()
    model_form = forms.VirtualDiskExtensionImportForm

class VirtualDiskExtensionChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VirtualDiskExtension.objects.all()


#
# VirtualSwitch
#
class VirtualSwitchListView(generic.ObjectListView):
    queryset = models.VirtualSwitch.objects.all()
    filterset = filtersets.VirtualSwitchFilterSet
    table = tables.VirtualSwitchTable

class VirtualSwitchView(generic.ObjectView):
    queryset = models.VirtualSwitch.objects.all()

class VirtualSwitchEditView(generic.ObjectEditView):
    queryset = models.VirtualSwitch.objects.all()
    form = forms.VirtualSwitchForm

class VirtualSwitchDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualSwitch.objects.all()

class VirtualSwitchBulkEditView(generic.BulkEditView):
    queryset = models.VirtualSwitch.objects.all()
    filterset = filtersets.VirtualSwitchFilterSet
    table = tables.VirtualSwitchTable
    form = forms.VirtualSwitchBulkEditForm

class VirtualSwitchBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VirtualSwitch.objects.all()
    filterset = filtersets.VirtualSwitchFilterSet
    table = tables.VirtualSwitchTable

class VirtualSwitchImportView(generic.BulkImportView):
    queryset = models.VirtualSwitch.objects.all()
    model_form = forms.VirtualSwitchImportForm

class VirtualSwitchChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VirtualSwitch.objects.all()


#
# VirtualNetwork
#
class VirtualNetworkListView(generic.ObjectListView):
    queryset = models.VirtualNetwork.objects.all()
    filterset = filtersets.VirtualNetworkFilterSet
    table = tables.VirtualNetworkTable

class VirtualNetworkView(generic.ObjectView):
    queryset = models.VirtualNetwork.objects.all()

class VirtualNetworkEditView(generic.ObjectEditView):
    queryset = models.VirtualNetwork.objects.all()
    form = forms.VirtualNetworkForm

class VirtualNetworkDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualNetwork.objects.all()

class VirtualNetworkBulkEditView(generic.BulkEditView):
    queryset = models.VirtualNetwork.objects.all()
    filterset = filtersets.VirtualNetworkFilterSet
    table = tables.VirtualNetworkTable
    form = forms.VirtualNetworkBulkEditForm

class VirtualNetworkBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VirtualNetwork.objects.all()
    filterset = filtersets.VirtualNetworkFilterSet
    table = tables.VirtualNetworkTable

class VirtualNetworkImportView(generic.BulkImportView):
    queryset = models.VirtualNetwork.objects.all()
    model_form = forms.VirtualNetworkImportForm

class VirtualNetworkChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VirtualNetwork.objects.all()


#
# VirtualSwitchUplink
#
class VirtualSwitchUplinkListView(generic.ObjectListView):
    queryset = models.VirtualSwitchUplink.objects.all()
    filterset = filtersets.VirtualSwitchUplinkFilterSet
    table = tables.VirtualSwitchUplinkTable

class VirtualSwitchUplinkView(generic.ObjectView):
    queryset = models.VirtualSwitchUplink.objects.all()

class VirtualSwitchUplinkEditView(generic.ObjectEditView):
    queryset = models.VirtualSwitchUplink.objects.all()
    form = forms.VirtualSwitchUplinkForm

class VirtualSwitchUplinkDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualSwitchUplink.objects.all()

class VirtualSwitchUplinkBulkEditView(generic.BulkEditView):
    queryset = models.VirtualSwitchUplink.objects.all()
    filterset = filtersets.VirtualSwitchUplinkFilterSet
    table = tables.VirtualSwitchUplinkTable
    form = forms.VirtualSwitchUplinkBulkEditForm

class VirtualSwitchUplinkBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VirtualSwitchUplink.objects.all()
    filterset = filtersets.VirtualSwitchUplinkFilterSet
    table = tables.VirtualSwitchUplinkTable

class VirtualSwitchUplinkImportView(generic.BulkImportView):
    queryset = models.VirtualSwitchUplink.objects.all()
    model_form = forms.VirtualSwitchUplinkImportForm

class VirtualSwitchUplinkChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VirtualSwitchUplink.objects.all()


#
# VMInterfaceExtension
#
class VMInterfaceExtensionListView(generic.ObjectListView):
    queryset = models.VMInterfaceExtension.objects.all()
    filterset = filtersets.VMInterfaceExtensionFilterSet
    table = tables.VMInterfaceExtensionTable

class VMInterfaceExtensionView(generic.ObjectView):
    queryset = models.VMInterfaceExtension.objects.all()

class VMInterfaceExtensionEditView(generic.ObjectEditView):
    queryset = models.VMInterfaceExtension.objects.all()
    form = forms.VMInterfaceExtensionForm

class VMInterfaceExtensionDeleteView(generic.ObjectDeleteView):
    queryset = models.VMInterfaceExtension.objects.all()

class VMInterfaceExtensionBulkEditView(generic.BulkEditView):
    queryset = models.VMInterfaceExtension.objects.all()
    filterset = filtersets.VMInterfaceExtensionFilterSet
    table = tables.VMInterfaceExtensionTable
    form = forms.VMInterfaceExtensionBulkEditForm

class VMInterfaceExtensionBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VMInterfaceExtension.objects.all()
    filterset = filtersets.VMInterfaceExtensionFilterSet
    table = tables.VMInterfaceExtensionTable

class VMInterfaceExtensionImportView(generic.BulkImportView):
    queryset = models.VMInterfaceExtension.objects.all()
    model_form = forms.VMInterfaceExtensionImportForm

class VMInterfaceExtensionChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VMInterfaceExtension.objects.all()


#
# ResourcePool
#
class ResourcePoolListView(generic.ObjectListView):
    queryset = models.ResourcePool.objects.all()
    filterset = filtersets.ResourcePoolFilterSet
    table = tables.ResourcePoolTable

class ResourcePoolView(generic.ObjectView):
    queryset = models.ResourcePool.objects.all()

class ResourcePoolEditView(generic.ObjectEditView):
    queryset = models.ResourcePool.objects.all()
    form = forms.ResourcePoolForm

class ResourcePoolDeleteView(generic.ObjectDeleteView):
    queryset = models.ResourcePool.objects.all()

class ResourcePoolBulkEditView(generic.BulkEditView):
    queryset = models.ResourcePool.objects.all()
    filterset = filtersets.ResourcePoolFilterSet
    table = tables.ResourcePoolTable
    form = forms.ResourcePoolBulkEditForm

class ResourcePoolBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ResourcePool.objects.all()
    filterset = filtersets.ResourcePoolFilterSet
    table = tables.ResourcePoolTable

class ResourcePoolImportView(generic.BulkImportView):
    queryset = models.ResourcePool.objects.all()
    model_form = forms.ResourcePoolImportForm

class ResourcePoolChangeLogView(generic.ObjectChangeLogView):
    queryset = models.ResourcePool.objects.all()


#
# ResourceScheduling
#
class ResourceSchedulingListView(generic.ObjectListView):
    queryset = models.ResourceScheduling.objects.all()
    filterset = filtersets.ResourceSchedulingFilterSet
    table = tables.ResourceSchedulingTable

class ResourceSchedulingView(generic.ObjectView):
    queryset = models.ResourceScheduling.objects.all()

class ResourceSchedulingEditView(generic.ObjectEditView):
    queryset = models.ResourceScheduling.objects.all()
    form = forms.ResourceSchedulingForm

class ResourceSchedulingDeleteView(generic.ObjectDeleteView):
    queryset = models.ResourceScheduling.objects.all()

class ResourceSchedulingBulkEditView(generic.BulkEditView):
    queryset = models.ResourceScheduling.objects.all()
    filterset = filtersets.ResourceSchedulingFilterSet
    table = tables.ResourceSchedulingTable
    form = forms.ResourceSchedulingBulkEditForm

class ResourceSchedulingBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ResourceScheduling.objects.all()
    filterset = filtersets.ResourceSchedulingFilterSet
    table = tables.ResourceSchedulingTable

class ResourceSchedulingImportView(generic.BulkImportView):
    queryset = models.ResourceScheduling.objects.all()
    model_form = forms.ResourceSchedulingImportForm

class ResourceSchedulingChangeLogView(generic.ObjectChangeLogView):
    queryset = models.ResourceScheduling.objects.all()


#
# HighAvailability
#
class HighAvailabilityListView(generic.ObjectListView):
    queryset = models.HighAvailability.objects.all()
    filterset = filtersets.HighAvailabilityFilterSet
    table = tables.HighAvailabilityTable

class HighAvailabilityView(generic.ObjectView):
    queryset = models.HighAvailability.objects.all()

class HighAvailabilityEditView(generic.ObjectEditView):
    queryset = models.HighAvailability.objects.all()
    form = forms.HighAvailabilityForm

class HighAvailabilityDeleteView(generic.ObjectDeleteView):
    queryset = models.HighAvailability.objects.all()

class HighAvailabilityBulkEditView(generic.BulkEditView):
    queryset = models.HighAvailability.objects.all()
    filterset = filtersets.HighAvailabilityFilterSet
    table = tables.HighAvailabilityTable
    form = forms.HighAvailabilityBulkEditForm

class HighAvailabilityBulkDeleteView(generic.BulkDeleteView):
    queryset = models.HighAvailability.objects.all()
    filterset = filtersets.HighAvailabilityFilterSet
    table = tables.HighAvailabilityTable

class HighAvailabilityImportView(generic.BulkImportView):
    queryset = models.HighAvailability.objects.all()
    model_form = forms.HighAvailabilityImportForm

class HighAvailabilityChangeLogView(generic.ObjectChangeLogView):
    queryset = models.HighAvailability.objects.all()
