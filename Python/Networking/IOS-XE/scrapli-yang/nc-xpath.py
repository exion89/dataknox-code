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

ospf_xpath = '/ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id="235802126"]/ospf-area[area-id=599]/ospf-interface[name="Loopback14"]'
response = conn.get(
    filter_=ospf_xpath, filter_type='xpath')
print(response.result)
