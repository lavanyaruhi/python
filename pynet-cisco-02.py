from netmiko import ConnectHandler

#First create the device object using a dictionary
CSR = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port":22
}

# Next establish the SSH connection
net_connect = ConnectHandler(**CSR,banner_timeout=100,timeout=100,auth_timeout=1000)

# Then send the command and print the output

output = net_connect.send_command('show clock')

print(output)

# Finally close the connection
net_connect.disconnect()
