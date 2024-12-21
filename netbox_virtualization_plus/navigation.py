from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

storage_items = (
    PluginMenuItem(
        link='plugins:netbox_virtualization_plus:datastore_list',
        link_text='Datastores',
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:datastore_add',
                title='Add Datastore',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:datastore_import',
                title='Import Datastores',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
)
network_items = (
    PluginMenuItem(
        link='plugins:netbox_virtualization_plus:virtualswitch_list',
        link_text='Virtual Switches',
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:virtualswitch_add',
                title='Add Virtual Switch',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:virtualswitch_import',
                title='Import Virtual Switches',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:netbox_virtualization_plus:virtualnetwork_list',
        link_text='Virtual Networks',
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:virtualnetwork_add',
                title='Add Virtual Network',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:virtualnetwork_import',
                title='Import Virtual Networks',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
)
management_items = (
    PluginMenuItem(
        link='plugins:netbox_virtualization_plus:resourcepool_list',
        link_text='Resource Pools',
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:resourcepool_add',
                title='Add Resource Pool',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:resourcepool_import',
                title='Import Resource Pools',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:netbox_virtualization_plus:resourcescheduling_list',
        link_text='Resource Scheduling',
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:resourcescheduling_add',
                title='Add Resource Scheduling',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:resourcescheduling_import',
                title='Import Schedulings',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:netbox_virtualization_plus:highavailability_list',
        link_text='HA Configs',
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:highavailability_add',
                title='Add HA Config',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:netbox_virtualization_plus:highavailability_import',
                title='Import HA Configs',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
)

# Define the top-level menu with icon
menu = PluginMenu(
    label="Virtualization+",
    groups=(("Storage", storage_items),("Network", network_items), ("Management", management_items)),
    icon_class="mdi mdi-server",
)