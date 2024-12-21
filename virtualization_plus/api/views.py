from netbox.api.viewsets import NetBoxModelViewSet
import virtualization_plus.models as models
import virtualization_plus.filtersets as filtersets
import virtualization_plus.api.serializers as serializers

class VMSnapshotViewSet(NetBoxModelViewSet):
    queryset = models.VMSnapshot.objects.all()
    serializer_class = serializers.VMSnapshotSerializer
    filterset_class = filtersets.VMSnapshotFilterSet
    
class DatastoreViewSet(NetBoxModelViewSet):
    queryset = models.Datastore.objects.all()
    serializer_class = serializers.DatastoreSerializer
    filterset_class = filtersets.DatastoreFilterSet

class VirtualDiskExtensionViewSet(NetBoxModelViewSet):
    queryset = models.VirtualDiskExtension.objects.all()
    serializer_class = serializers.VirtualDiskExtensionSerializer
    filterset_class = filtersets.VirtualDiskExtensionFilterSet

class VirtualSwitchViewSet(NetBoxModelViewSet):
    queryset = models.VirtualSwitch.objects.all()
    serializer_class = serializers.VirtualSwitchSerializer
    filterset_class = filtersets.VirtualSwitchFilterSet

class VirtualNetworkViewSet(NetBoxModelViewSet):
    queryset = models.VirtualNetwork.objects.all()
    serializer_class = serializers.VirtualNetworkSerializer
    filterset_class = filtersets.VirtualNetworkFilterSet

class VirtualSwitchUplinkViewSet(NetBoxModelViewSet):
    queryset = models.VirtualSwitchUplink.objects.all()
    serializer_class = serializers.VirtualSwitchUplinkSerializer
    filterset_class = filtersets.VirtualSwitchUplinkFilterSet

class VMInterfaceExtensionViewSet(NetBoxModelViewSet):
    queryset = models.VMInterfaceExtension.objects.all()
    serializer_class = serializers.VMInterfaceExtensionSerializer
    filterset_class = filtersets.VMInterfaceExtensionFilterSet

class ResourcePoolViewSet(NetBoxModelViewSet):
    queryset = models.ResourcePool.objects.all()
    serializer_class = serializers.ResourcePoolSerializer
    filterset_class = filtersets.ResourcePoolFilterSet

class ResourceSchedulingViewSet(NetBoxModelViewSet):
    queryset = models.ResourceScheduling.objects.all()
    serializer_class = serializers.ResourceSchedulingSerializer
    filterset_class = filtersets.ResourceSchedulingFilterSet

class HighAvailabilityViewSet(NetBoxModelViewSet):
    queryset = models.HighAvailability.objects.all()
    serializer_class = serializers.HighAvailabilitySerializer
    filterset_class = filtersets.HighAvailabilityFilterSet
