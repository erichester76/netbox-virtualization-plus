from netbox.plugins import PluginConfig

__author__ = "Eric Hester"
__email__ = "hester1@clemson.edu"
__version__ = "0.1"

class VirtualizationPlusConfig(PluginConfig):
    name = 'netbox_virtualization_plus'
    verbose_name = 'Virtualization+'
    description = 'Additional virtualization features'
    version = '0.1'
    min_version = '4.0.0'
    max_version = '4.2.0'
    default_auto_field = 'django.db.models.AutoField'

config = VirtualizationPlusConfig
