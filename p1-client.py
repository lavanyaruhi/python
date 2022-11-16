import socket

#creating a socket object
s=socket.socket()

#Define the port number in which we want to connect

port=2357

# connect to the server on local computer
s.connect(('127.0.0.1',port))

#recieve data from the server
print(s.recv(1024))  # calling s.recv(1024) returns more data without the socket on the other side doing s.send(data)
s.close()  #connectionrefusederror:no connection could
