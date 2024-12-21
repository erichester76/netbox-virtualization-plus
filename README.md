# NetBox Virtualization+ Plugin

**Virtualization+** is a NetBox plugin providing additional virtualization management features. This includes:

- Datastores
- VM Snapshots
- Distributed Virtual Switches (DVS)
- Virtual Gateways
- Resource Groups
- DRS/HA Configuration

## Features
- CRUD UI for each additional model
- Bulk edit/delete, CSV import, and changelog
- API endpoints following NetBox conventions

## Requirements
- NetBox >= 3.4, <3.6 (adjust as required)
- Python 3.8+ (adjust as required)

## Installation

1. **Clone** or **download** this repository, then navigate into it:
   ```bash
   cd netbox-virtualization-plus
   ```

2. **Install** the plugin:
   ```bash
   pip install .
   ```
   Or install via `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Enable** the plugin in `configuration.py` (NetBox config):
   ```python
   PLUGINS = [
       'virtualization_plus',  # or 'netbox_virtualization_plus' if named differently
   ]
   PLUGINS_CONFIG = {
       'virtualization_plus': {
           # Plugin-specific settings here
       }
   }
   ```

4. **Restart** NetBox services:
   ```bash
   sudo systemctl restart netbox
   ```

## Usage
After installation, the plugin’s models will appear under Plugins → Virtualization+ in the NetBox UI.

## Contributing
- Pull requests are welcome.
- Feel free to open issues for bugs or feature requests.

## License
Apache-2.0

