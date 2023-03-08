#!/usr/bin/python3
import os
import subprocess
current_dir = os.getcwd()
filename='perfcheck.py'
file_loc = current_dir+'/'+filename
print(file_loc)
#locust -f perfcheck.py --headless -u 20 -r 2 -t 10
users=20
rate=2
time=10 #seconds
locust_cmd=["locust","-f","./perfcheck.py",\
    "--headless","-u",f"{users}","-r",f"{rate}","-t",f"{time}"]
subprocess.run(locust_cmd)