#!/usr/bin/env python
import os
import psutil
from datetime import datetime
import time

#if file does not exist, create the file
file = open('status.log','w+')

def print_interval(x):
    y = 0
    while x != y:
        a= str(psutil.cpu_times())+','+str(datetime.now())
        file.writelines(a+'\n')
        b= ("memory_virtual=%s,memory_swap=%s,%s\n")%(psutil.virtual_memory(), psutil.swap_memory(),datetime.now())
        file.writelines(b+'\n')
        time.sleep(1)
        y = 1+y

    else:
        pass




#Check on current computer cpu usage and available memory
#psutil.cpu_times

#check on current memory
#psutil.virtual_memory()

#psutil.swap_memory()

#disk
#psutil.disk_usage('/')
#psutil.disk_io_counters(perdisk=False)

#check on network
#psutil.net_io_counters(pernic=True)
#psutil.net_if_addrs()

print_interval(10)
file.close()

