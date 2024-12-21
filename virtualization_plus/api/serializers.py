from netbox.api.serializers import NetBoxModelSerializer
import virtualization_plus.models as models

class VMSnapshotSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VMSnapshot
        fields = '__all__'
        
class DatastoreSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.Datastore
        fields = '__all__'

class VirtualDiskExtensionSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VirtualDiskExtension
        fields = '__all__'

class VirtualSwitchSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VirtualSwitch
        fields = '__all__'

class VirtualNetworkSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VirtualNetwork
        fields = '__all__'

class VirtualSwitchUplinkSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VirtualSwitchUplink
        fields = '__all__'

class VMInterfaceExtensionSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VMInterfaceExtension
        fields = '__all__'

class ResourcePoolSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.ResourcePool
        fields = '__all__'

class ResourceSchedulingSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.ResourceScheduling
        fields = '__all__'

class HighAvailabilitySerializer(NetBoxModelSerializer):
    class Meta:
        model = models.HighAvailability
        fields = '__all__'
