from ncclient import manager
import xmltodict
import xml.dom.minidom

int_filter = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
"""

with manager.connect(host="sandbox-iosxe-latest-1.cisco.com", port="830", username="developer", password="C1sco12345", hostkey_verify=False) as m:
    netconf_response = m.get_config(source='running', filter=('subtree', int_filter))

python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
config = python_response["interfaces"]["interface"]

print(xml.dom.minidom.parseString(netconf_response.xml).toprettyxml())