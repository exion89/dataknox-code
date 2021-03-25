from scrapli_netconf.driver import NetconfScrape

my_device = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfScrape(**my_device)
conn.open()

ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
  <ospf-state>
    <ospf-instance>
        <af>address-family-ipv4</af>
        <router-id>235802126</router-id>
          <ospf-area>
            <area-id>599</area-id>
            <ospf-interface>
               <name>Loopback14</name>
            </ospf-interface>
          </ospf-area>
    </ospf-instance>
  </ospf-state>
</ospf-oper-data>
"""

response = conn.get(
    filter_=ospf_filter, filter_type='subtree')
print(response.result)
