# an example script to connect to google using socket
import socket # for socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 443 # https
#port =80 # http
#port=27

try:
    host_ip = socket.gethostbyname('www.google.co.in') # endpoint
    # gethostbyname() --map a hostname to its IP address
except socket.gaierror:   # get address information error

# this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))


print(host_ip)
print ("the socket has successfully connected to google")
