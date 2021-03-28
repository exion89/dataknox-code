from ncclient import manager
from router_info import router

config_template = open(
    "C:/Users/samlu/Stuff/gitrepo/dataknox-code/Python/Networking/IOS-XE/ios_config.xml").read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="test interface")

with manager.connect(**router, hostkey_verify=False) as m:
    response = m.edit_config(netconf_config, target="running")

print(response)
