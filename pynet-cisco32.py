from netmiko import ConnectHandler
import pdb
#First create the device object using a dictionary

Router = {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345", #without this no authentication available
        "port":22
    }
net_connect=ConnectHandler(**Router)
# descover the hostname from the prompt
hostname=net_connect.send_command('show run | i host')
hostname.split(" ")

#hostname, devices=hostname.split(" ")


hostname, devices, *rest = hostname.split(" ")
print(hostname)
print(devices)
#print(rest)
print("Backing up " + devices)

filename='C:/Users/USER431/PycharmProjects/projPython/device.txt'

showrun=net_connect.send_command('show run')
showvlan=net_connect.send_command('show vlan')
showver=net_connect.send_command('show ver')
log_file=open(filename, "a") # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write((showver))
log_file.write("\n")
net_connect.disconnect()
