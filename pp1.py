import socket
print(socket.gethostname())


import os
print(os.system("ipconfig"))


hostname=socket.gethostname()
ipad=socket.gethostbyname(hostname)
print(ipad)
