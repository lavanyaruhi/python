import socket

s=socket.socket()
port=2357  #0-1200 port is recieved for system protocols
s.bind(('',port))  #'':ip address,open: take request from any machine in the network, bind()---2.
print("Socket blocked to %s"%(port))

s.listen(5)
print("Socket is listening")

while True:
    c, addr=s.accept()
    print('Got connection from',addr)  #addr has the client side port number
    c.send(b'Thank you for connecting')  #bytes.decode()
    c.close()  #listen from new client
