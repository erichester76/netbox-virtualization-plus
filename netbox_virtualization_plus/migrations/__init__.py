# Generated by Django 5.0.10 on 2024-12-21 23:08

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0191_module_bay_rebuild'),
        ('extras', '0121_customfield_related_object_filter'),
        ('ipam', '0070_vlangroup_vlan_id_ranges'),
        ('virtualization', '0040_convert_disk_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datastore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('capacity_gb', models.DecimalField(decimal_places=2, max_digits=12)),
                ('used_gb', models.DecimalField(decimal_places=2, max_digits=12)),
                ('datastore_type', models.CharField(blank=True, max_length=50)),
                ('mount_point', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cluster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='datastores', to='virtualization.cluster')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='datastores', to='dcim.device')),
                ('storage_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='datastore_attachments', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HighAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('enabled', models.BooleanField(default=False)),
                ('failover_level', models.PositiveIntegerField(default=1)),
                ('admission_control_enabled', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('cluster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='high_availability', to='virtualization.cluster')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResourcePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('pool_type', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resource_pools', to='virtualization.cluster')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResourceScheduling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('enabled', models.BooleanField(default=False)),
                ('automation_level', models.CharField(blank=True, max_length=50)),
                ('imbalance_threshold', models.IntegerField(default=5)),
                ('description', models.TextField(blank=True)),
                ('cluster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resource_scheduling', to='virtualization.cluster')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VirtualDiskExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('notes', models.TextField(blank=True)),
                ('datastore', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='virtual_disks', to='netbox_virtualization_plus.datastore')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtual_disk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_extension', to='virtualization.virtualdisk')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VirtualSwitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('switch_type', models.CharField(blank=True, max_length=50)),
                ('version', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='virtual_switches', to='virtualization.cluster')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VirtualNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('trunk_allowed_vlans', models.CharField(blank=True, max_length=200)),
                ('network_type', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtual_switch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='virtual_networks', to='netbox_virtualization_plus.virtualswitch')),
            ],
            options={
                'unique_together': {('virtual_switch', 'name')},
            },
        ),
        migrations.CreateModel(
            name='VirtualSwitchUplink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('lacp_enabled', models.BooleanField(default=False)),
                ('teaming_policy', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='virtual_switch_uplinks', to='dcim.interface')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtual_switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uplinks', to='netbox_virtualization_plus.virtualswitch')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VMInterfaceExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('notes', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtual_network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='netbox_virtualization_plus.virtualnetwork')),
                ('vlan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ipam.vlan')),
                ('vm_interface', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_extension', to='virtualization.vminterface')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VMSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('size_gb', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('memory_included', models.BooleanField(default=False)),
                ('snapshot_type', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtual_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snapshots', to='virtualization.virtualmachine')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]