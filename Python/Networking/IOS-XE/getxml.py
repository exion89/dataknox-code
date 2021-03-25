from ncclient import manager
import xmltodict

with manager.connect(host="sandbox-iosxe-latest-1.cisco.com", port="830", username="developer", password="C1sco12345", hostkey_verify=False) as m:
    xml_config = m.get_config(source='running').data_xml

for c in m.server_capabilities:
    print(c)
