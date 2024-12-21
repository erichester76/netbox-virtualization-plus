from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

items = (
    PluginMenuItem(
        link='plugins:virtualization_plus:datastore_list',
        link_text='Datastores',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:datastore_add',
                title='Add Datastore',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:datastore_import',
                title='Import Datastores',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:virtualdiskextension_list',
        link_text='Virtual Disk Extensions',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualdiskextension_add',
                title='Add Disk Extension',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualdiskextension_import',
                title='Import Disk Extensions',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:virtualswitch_list',
        link_text='Virtual Switches',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualswitch_add',
                title='Add Virtual Switch',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualswitch_import',
                title='Import Virtual Switches',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:virtualnetwork_list',
        link_text='Virtual Networks',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualnetwork_add',
                title='Add Virtual Network',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualnetwork_import',
                title='Import Virtual Networks',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:virtualswitchuplink_list',
        link_text='Switch Uplinks',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualswitchuplink_add',
                title='Add Switch Uplink',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:virtualswitchuplink_import',
                title='Import Switch Uplinks',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:vminterfaceextension_list',
        link_text='VM Interface Extensions',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:vminterfaceextension_add',
                title='Add Interface Extension',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:vminterfaceextension_import',
                title='Import Interface Extensions',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:resourcepool_list',
        link_text='Resource Pools',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:resourcepool_add',
                title='Add Resource Pool',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:resourcepool_import',
                title='Import Resource Pools',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:resourcescheduling_list',
        link_text='Resource Scheduling',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:resourcescheduling_add',
                title='Add Resource Scheduling',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:resourcescheduling_import',
                title='Import Schedulings',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
    PluginMenuItem(
        link='plugins:virtualization_plus:highavailability_list',
        link_text='HA Configs',
        buttons=[
            PluginMenuButton(
                link='plugins:virtualization_plus:highavailability_add',
                title='Add HA Config',
                icon_class='mdi mdi-plus-thick',
            ),
            PluginMenuButton(
                link='plugins:virtualization_plus:highavailability_import',
                title='Import HA Configs',
                icon_class='mdi mdi-upload',
            )
        ]
    ),
)

# Define the top-level menu with icon
menu = PluginMenu(
    label="Virtualization+",
    groups=(("Virtualization", items),),
    icon_class="mdi mdi-server",
)