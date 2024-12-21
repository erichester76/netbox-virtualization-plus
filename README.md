# NetBox Virtualization+ Plugin

**Virtualization+** is a NetBox plugin providing additional virtualization management features. This includes:

- VM Snapshots
- Virtual Switches / Networks
- Datastores
- Resource Groups
- DRS/HA Configuration

## Requirements
- NetBox >= 4.0, <=4.2 
- Python 3.8+ 

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
       'netbox_virtualization_plus',  
   ]
   PLUGINS_CONFIG = {
       'netbox_virtualization_plus': {
           # Plugin-specific settings here
       }
   }
   ```

4. **Restart** NetBox services:
   ```bash
   sudo systemctl restart netbox
   ```

## Usage
After installation, the plugin’s models will appear under Virtualization+ in the NetBox UI.

## Contributing
- Pull requests are welcome.
- Feel free to open issues for bugs or feature requests.

## License
Apache-2.0

