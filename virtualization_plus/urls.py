from django.urls import path
import virtualization_plus.views as views

app_name = 'virtualization_plus'

urlpatterns = [
    # VMSnapshot
    path('vm-snapshots/', views.VMSnapshotListView.as_view(), name='vmsnapshot_list'),
    path('vm-snapshots/add/', views.VMSnapshotEditView.as_view(), name='vmsnapshot_add'),
    path('vm-snapshots/import/', views.VMSnapshotImportView.as_view(), name='vmsnapshot_import'),
    path('vm-snapshots/edit/', views.VMSnapshotBulkEditView.as_view(), name='vmsnapshot_bulk_edit'),
    path('vm-snapshots/delete/', views.VMSnapshotBulkDeleteView.as_view(), name='vmsnapshot_bulk_delete'),
    path('vm-snapshots/<int:pk>/', views.VMSnapshotView.as_view(), name='vmsnapshot'),
    path('vm-snapshots/<int:pk>/edit/', views.VMSnapshotEditView.as_view(), name='vmsnapshot_edit'),
    path('vm-snapshots/<int:pk>/delete/', views.VMSnapshotDeleteView.as_view(), name='vmsnapshot_delete'),
    path('vm-snapshots/<int:pk>/changelog/', views.VMSnapshotChangeLogView.as_view(), name='vmsnapshot_changelog'),

    # Datastore
    path('datastores/', views.DatastoreListView.as_view(), name='datastore_list'),
    path('datastores/add/', views.DatastoreEditView.as_view(), name='datastore_add'),
    path('datastores/import/', views.DatastoreImportView.as_view(), name='datastore_import'),
    path('datastores/edit/', views.DatastoreBulkEditView.as_view(), name='datastore_bulk_edit'),
    path('datastores/delete/', views.DatastoreBulkDeleteView.as_view(), name='datastore_bulk_delete'),
    path('datastores/<int:pk>/', views.DatastoreView.as_view(), name='datastore'),
    path('datastores/<int:pk>/edit/', views.DatastoreEditView.as_view(), name='datastore_edit'),
    path('datastores/<int:pk>/delete/', views.DatastoreDeleteView.as_view(), name='datastore_delete'),
    path('datastores/<int:pk>/changelog/', views.DatastoreChangeLogView.as_view(), name='datastore_changelog'),

    # VirtualDiskExtension
    path('v-disks/', views.VirtualDiskExtensionListView.as_view(), name='virtualdiskextension_list'),
    path('v-disks/add/', views.VirtualDiskExtensionEditView.as_view(), name='virtualdiskextension_add'),
    path('v-disks/import/', views.VirtualDiskExtensionImportView.as_view(), name='virtualdiskextension_import'),
    path('v-disks/edit/', views.VirtualDiskExtensionBulkEditView.as_view(), name='virtualdiskextension_bulk_edit'),
    path('v-disks/delete/', views.VirtualDiskExtensionBulkDeleteView.as_view(), name='virtualdiskextension_bulk_delete'),
    path('v-disks/<int:pk>/', views.VirtualDiskExtensionView.as_view(), name='virtualdiskextension'),
    path('v-disks/<int:pk>/edit/', views.VirtualDiskExtensionEditView.as_view(), name='virtualdiskextension_edit'),
    path('v-disks/<int:pk>/delete/', views.VirtualDiskExtensionDeleteView.as_view(), name='virtualdiskextension_delete'),
    path('v-disks/<int:pk>/changelog/', views.VirtualDiskExtensionChangeLogView.as_view(), name='virtualdiskextension_changelog'),

    # VirtualSwitch
    path('v-switches/', views.VirtualSwitchListView.as_view(), name='virtualswitch_list'),
    path('v-switches/add/', views.VirtualSwitchEditView.as_view(), name='virtualswitch_add'),
    path('v-switches/import/', views.VirtualSwitchImportView.as_view(), name='virtualswitch_import'),
    path('v-switches/edit/', views.VirtualSwitchBulkEditView.as_view(), name='virtualswitch_bulk_edit'),
    path('v-switches/delete/', views.VirtualSwitchBulkDeleteView.as_view(), name='virtualswitch_bulk_delete'),
    path('v-switches/<int:pk>/', views.VirtualSwitchView.as_view(), name='virtualswitch'),
    path('v-switches/<int:pk>/edit/', views.VirtualSwitchEditView.as_view(), name='virtualswitch_edit'),
    path('v-switches/<int:pk>/delete/', views.VirtualSwitchDeleteView.as_view(), name='virtualswitch_delete'),
    path('v-switches/<int:pk>/changelog/', views.VirtualSwitchChangeLogView.as_view(), name='virtualswitch_changelog'),

    # VirtualNetwork
    path('v-networks/', views.VirtualNetworkListView.as_view(), name='virtualnetwork_list'),
    path('v-networks/add/', views.VirtualNetworkEditView.as_view(), name='virtualnetwork_add'),
    path('v-networks/import/', views.VirtualNetworkImportView.as_view(), name='virtualnetwork_import'),
    path('v-networks/edit/', views.VirtualNetworkBulkEditView.as_view(), name='virtualnetwork_bulk_edit'),
    path('v-networks/delete/', views.VirtualNetworkBulkDeleteView.as_view(), name='virtualnetwork_bulk_delete'),
    path('v-networks/<int:pk>/', views.VirtualNetworkView.as_view(), name='virtualnetwork'),
    path('v-networks/<int:pk>/edit/', views.VirtualNetworkEditView.as_view(), name='virtualnetwork_edit'),
    path('v-networks/<int:pk>/delete/', views.VirtualNetworkDeleteView.as_view(), name='virtualnetwork_delete'),
    path('v-networks/<int:pk>/changelog/', views.VirtualNetworkChangeLogView.as_view(), name='virtualnetwork_changelog'),

    # VirtualSwitchUplink
    path('v-uplinks/', views.VirtualSwitchUplinkListView.as_view(), name='virtualswitchuplink_list'),
    path('v-uplinks/add/', views.VirtualSwitchUplinkEditView.as_view(), name='virtualswitchuplink_add'),
    path('v-uplinks/import/', views.VirtualSwitchUplinkImportView.as_view(), name='virtualswitchuplink_import'),
    path('v-uplinks/edit/', views.VirtualSwitchUplinkBulkEditView.as_view(), name='virtualswitchuplink_bulk_edit'),
    path('v-uplinks/delete/', views.VirtualSwitchUplinkBulkDeleteView.as_view(), name='virtualswitchuplink_bulk_delete'),
    path('v-uplinks/<int:pk>/', views.VirtualSwitchUplinkView.as_view(), name='virtualswitchuplink'),
    path('v-uplinks/<int:pk>/edit/', views.VirtualSwitchUplinkEditView.as_view(), name='virtualswitchuplink_edit'),
    path('v-uplinks/<int:pk>/delete/', views.VirtualSwitchUplinkDeleteView.as_view(), name='virtualswitchuplink_delete'),
    path('v-uplinks/<int:pk>/changelog/', views.VirtualSwitchUplinkChangeLogView.as_view(), name='virtualswitchuplink_changelog'),

    # VMInterfaceExtension
    path('vm-interfaces/', views.VMInterfaceExtensionListView.as_view(), name='vminterfaceextension_list'),
    path('vm-interfaces/add/', views.VMInterfaceExtensionEditView.as_view(), name='vminterfaceextension_add'),
    path('vm-interfaces/import/', views.VMInterfaceExtensionImportView.as_view(), name='vminterfaceextension_import'),
    path('vm-interfaces/edit/', views.VMInterfaceExtensionBulkEditView.as_view(), name='vminterfaceextension_bulk_edit'),
    path('vm-interfaces/delete/', views.VMInterfaceExtensionBulkDeleteView.as_view(), name='vminterfaceextension_bulk_delete'),
    path('vm-interfaces/<int:pk>/', views.VMInterfaceExtensionView.as_view(), name='vminterfaceextension'),
    path('vm-interfaces/<int:pk>/edit/', views.VMInterfaceExtensionEditView.as_view(), name='vminterfaceextension_edit'),
    path('vm-interfaces/<int:pk>/delete/', views.VMInterfaceExtensionDeleteView.as_view(), name='vminterfaceextension_delete'),
    path('vm-interfaces/<int:pk>/changelog/', views.VMInterfaceExtensionChangeLogView.as_view(), name='vminterfaceextension_changelog'),

    # ResourcePool
    path('resource-pools/', views.ResourcePoolListView.as_view(), name='resourcepool_list'),
    path('resource-pools/add/', views.ResourcePoolEditView.as_view(), name='resourcepool_add'),
    path('resource-pools/import/', views.ResourcePoolImportView.as_view(), name='resourcepool_import'),
    path('resource-pools/edit/', views.ResourcePoolBulkEditView.as_view(), name='resourcepool_bulk_edit'),
    path('resource-pools/delete/', views.ResourcePoolBulkDeleteView.as_view(), name='resourcepool_bulk_delete'),
    path('resource-pools/<int:pk>/', views.ResourcePoolView.as_view(), name='resourcepool'),
    path('resource-pools/<int:pk>/edit/', views.ResourcePoolEditView.as_view(), name='resourcepool_edit'),
    path('resource-pools/<int:pk>/delete/', views.ResourcePoolDeleteView.as_view(), name='resourcepool_delete'),
    path('resource-pools/<int:pk>/changelog/', views.ResourcePoolChangeLogView.as_view(), name='resourcepool_changelog'),

    # ResourceScheduling
    path('resource-schedulings/', views.ResourceSchedulingListView.as_view(), name='resourcescheduling_list'),
    path('resource-schedulings/add/', views.ResourceSchedulingEditView.as_view(), name='resourcescheduling_add'),
    path('resource-schedulings/import/', views.ResourceSchedulingImportView.as_view(), name='resourcescheduling_import'),
    path('resource-schedulings/edit/', views.ResourceSchedulingBulkEditView.as_view(), name='resourcescheduling_bulk_edit'),
    path('resource-schedulings/delete/', views.ResourceSchedulingBulkDeleteView.as_view(), name='resourcescheduling_bulk_delete'),
    path('resource-schedulings/<int:pk>/', views.ResourceSchedulingView.as_view(), name='resourcescheduling'),
    path('resource-schedulings/<int:pk>/edit/', views.ResourceSchedulingEditView.as_view(), name='resourcescheduling_edit'),
    path('resource-schedulings/<int:pk>/delete/', views.ResourceSchedulingDeleteView.as_view(), name='resourcescheduling_delete'),
    path('resource-schedulings/<int:pk>/changelog/', views.ResourceSchedulingChangeLogView.as_view(), name='resourcescheduling_changelog'),

    # HighAvailability
    path('ha-configs/', views.HighAvailabilityListView.as_view(), name='highavailability_list'),
    path('ha-configs/add/', views.HighAvailabilityEditView.as_view(), name='highavailability_add'),
    path('ha-configs/import/', views.HighAvailabilityImportView.as_view(), name='highavailability_import'),
    path('ha-configs/edit/', views.HighAvailabilityBulkEditView.as_view(), name='highavailability_bulk_edit'),
    path('ha-configs/delete/', views.HighAvailabilityBulkDeleteView.as_view(), name='highavailability_bulk_delete'),
    path('ha-configs/<int:pk>/', views.HighAvailabilityView.as_view(), name='highavailability'),
    path('ha-configs/<int:pk>/edit/', views.HighAvailabilityEditView.as_view(), name='highavailability_edit'),
    path('ha-configs/<int:pk>/delete/', views.HighAvailabilityDeleteView.as_view(), name='highavailability_delete'),
    path('ha-configs/<int:pk>/changelog/', views.HighAvailabilityChangeLogView.as_view(), name='highavailability_changelog'),
]
