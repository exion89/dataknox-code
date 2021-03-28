import requests
import json

router = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": "9443",
    "user": "developer",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback69"

#payload = {
#     "ietf-interfaces:interface": {
#         "name": "Loopback69",
#         "description": "$GME Diamondhands",
#         "type": "iana-if-type:softwareLoopback",
#         "enabled": True,
#         "ietf-ip:ipv4": {
#             "address": [
#                 {
#                     "ip": "69.69.69.69",
#                     "netmask": "255.255.255.0"
#                 }
#             ]
#         }
#     }
# }

response = requests.delete(url=url, headers=headers, auth=(
    router['user'], router['password']), verify=False)

if response.status_code == 204:
    print(response)
    print(response.text)

#data=json.dumps(payload),