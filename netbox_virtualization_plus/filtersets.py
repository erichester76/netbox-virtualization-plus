import django_filters
from netbox.filtersets import NetBoxModelFilterSet
import netbox_virtualization_plus.models as models

class VMSnapshotFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search'
    )

    class Meta:
        model = models.VMSnapshot
        fields = ('id', 'name', 'virtual_machine', 'memory_included', 'snapshot_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(name__icontains=value)

class DatastoreFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(method='search', label='Search')

    class Meta:
        model = models.Datastore
        fields = ('id', 'name', 'cluster', 'host', 'datastore_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(name__icontains=value)


class VirtualDiskExtensionFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.VirtualDiskExtension
        fields = ('id', 'virtual_disk', 'datastore')


class VirtualSwitchFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(method='search', label='Search')

    class Meta:
        model = models.VirtualSwitch
        fields = ('id', 'name', 'cluster', 'switch_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(name__icontains=value)


class VirtualNetworkFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.VirtualNetwork
        fields = ('id', 'name', 'virtual_switch')


class VirtualSwitchUplinkFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.VirtualSwitchUplink
        fields = ('id', 'virtual_switch', 'interface')


class VMInterfaceExtensionFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.VMInterfaceExtension
        fields = ('id', 'vm_interface', 'virtual_network', 'vlan')


class ResourcePoolFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.ResourcePool
        fields = ('id', 'name', 'cluster', 'pool_type')


class ResourceSchedulingFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.ResourceScheduling
        fields = ('id', 'cluster', 'enabled', 'automation_level')


class HighAvailabilityFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.HighAvailability
        fields = ('id', 'cluster', 'enabled')
