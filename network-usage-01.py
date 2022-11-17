import os
import time
import pandas as pd
import psutil
import pdb
UPDATE_DELAY=1

def get_size(bytes):
    for unit in ['','K','M','G','T','P']: # Bynary mnemonics(k,m,g,t,p)
        if bytes < 1024:
            return f"{bytes:.2f} {unit} B"
        bytes /= 1024
io=psutil.net_io_counters(pernic=True)
print(io)
print('-'*50)
while True:
    time.sleep(UPDATE_DELAY)

    io_2=psutil.net_io_counters(pernic=True)
    print(io_2)
    print('-'*50)
    # initializing the data to gather to a list of dicts
    data=[]
    for iface, iface_io in io.items() :
        print(iface)
        print(iface_io)
        print(io_2[iface])
        # new -old stats gets us the speed
        upload_speed, download_speed=io_2[iface].bytes_sent-iface_io.bytes_sent, io_2[iface].bytes_recv-iface_io.bytes_recv
        data.append({
            "iface": iface, "Download":get_size(io_2[iface].bytes_recv),
            "Upload":get_size(io_2[iface].bytes_sent),
            "Upload speed": f"{get_size(upload_speed/ UPDATE_DELAY)}/s",
            "Download speed": f"{get_size(download_speed/ UPDATE_DELAY)}/s"
        })

    io=io_2
    # construct a pandas dataframe to print stats in a cool tabular style
    df=pd.DataFrame(data)
    # sort values from column, feel free to change the column
    df.sort_values("Download", inplace=True, ascending=False)
    #clear the screen based on your os
    os.system("cls") if "nt" in os.name else os.system("clear")

    print(df.to_string)