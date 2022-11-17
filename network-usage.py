

# network usage per process

from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd
# get all networks adaptor's mac address
all_macs={iface.mac for iface in ifaces.values()}
print(all_macs)
# a dictionary to map each connection id(pid) to total upload (0) and download (1) traffic
connection2pid={}
pid2traffic=defaultdict(lambda: [0,0])
print(pid2traffic)
# global pandas dataframe that used to track previous traffic status
global_df = None
# global boolean for status of program
is_program_running = True
# function with body -function declaration
# function with body - function definition
# function abstraction - declare the func + func[complete/partial] body/def - implimentator
def get_size(bytes):
    for unit in ['','K','M','G','T','P']: # Bynary mnemonics(k,m,g,t,p)
        if bytes < 1024:
            return f"{bytes:.2f} {unit} B"
        bytes /= 1024

