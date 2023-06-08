ip_addresses = ['192.168.0.1', '10.0.0.1', '172.16.0.1', '8.8.8.8']

private_ips = [ip for ip in ip_addresses if ip.startswith(('192.168.', '10.', '172.'))]

print(private_ips)