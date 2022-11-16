import os, ipaddress

os.system('cls') #clear the console or terminal at the start of the execution
while True:
    ip=input('Enter the address')
    try:              # condition that we need to check
        print(ipaddress.ip_address(ip))
        print('ip valid')
    except:            # try exception fails then it will executed
        print('-'*50)
        print('ip is not valid')
    finally:  # with/without exception -->finally block executed
        if ip =='quit':
            print('Script finished')
            break
