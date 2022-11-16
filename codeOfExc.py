
import os

with open("ip_list.txt") as file:
    park=file.read()
    park=park.splitlines()   # split each line as divided as a list
    print(" {park}  \n")
    print(park)
# ping for each ip in the file
for ip in park:
    response=os.popen(f'ping {ip}').read()
# saving some ping output details to output file

    if("Request timed out" or "unreacheble") in response:
        print(response)
        f=open("info_output.txt",'a')
        f.write(str(ip) + 'link is done' + '\n')
        f.close()
    else:
        print(response)
        f=open("info_output.txt",'a')
        f.write(str(ip) + 'is up ' + '\n')
        f.close()

with open('info_output.txt') as file:
    output=file.read()
    f.close()
    print(output)
with open('info_output.txt','w') as file:
    pass
