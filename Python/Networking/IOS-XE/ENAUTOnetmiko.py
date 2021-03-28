from netmiko import ConnectHandler
from dotenv import load_dotenv
load_dotenv()
router = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": 8181,
    "username": "developer",
    "password": "C1sco12345",
    "device_type": "cisco_ios"
}

configs = ['no int Lo101']                                    #'int loopback101', 'ip address 10.99.98.1 255.255.255.0', 'desc "Configured by Netmiko"', 'no shut']

try:
    c = ConnectHandler(**router)
    c.enable()
    c.send_config_set(configs)
    response = c.send_command("show ip int brief") #, use_textfsm=True)
    c.disconnect()
except Exception as ex:
    print(ex)
else:
    print(response)
