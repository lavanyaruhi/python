from netmiko import ConnectHandler

#First create the device object using a dictionary

with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345",
            "port":22
        }
        net_connect=ConnectHandler(**Router)

        print('Connecting to '+ IP)
        print('-'*76)
        output=net_connect.send_command('show ip int brief')
        print(output)
        print()
        print('-'*67)

net_connect.disconnect()