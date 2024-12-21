from rest_framework.routers import DefaultRouter
import virtualization_plus.api.views as api_views

router = DefaultRouter()

router.register('vm-snapshots', api_views.VMSnapshotViewSet)
router.register('datastores', api_views.DatastoreViewSet)
router.register('virtual-disk-extensions', api_views.VirtualDiskExtensionViewSet)
router.register('virtual-switches', api_views.VirtualSwitchViewSet)
router.register('virtual-networks', api_views.VirtualNetworkViewSet)
router.register('virtual-switch-uplinks', api_views.VirtualSwitchUplinkViewSet)
router.register('vm-interface-extensions', api_views.VMInterfaceExtensionViewSet)
router.register('resource-pools', api_views.ResourcePoolViewSet)
router.register('resource-schedulings', api_views.ResourceSchedulingViewSet)
router.register('ha-configs', api_views.HighAvailabilityViewSet)

urlpatterns = router.urls
