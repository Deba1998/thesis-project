#!/usr/bin/python3
import argparse
import metrohash
from datetime import datetime
from config import write_config
import os
import subprocess
from client_demo import clientRun

parser = argparse.ArgumentParser(prog='./main.py',\
description='To figure out system level bottleneck for REST API based services')
parser.add_argument('-l','--lower_bound_users',required=True,type=int)
parser.add_argument('-u','--upper_bound_users',required=True,type=int)
parser.add_argument('-s','--step_size',required=True,type=int)
parser.add_argument('-t','--run_time_script',default=60,type=int)
args = parser.parse_args()
print(args.lower_bound_users,args.upper_bound_users,args.step_size,args.run_time_script)
lower_bound=args.lower_bound_users
upper_bound=args.upper_bound_users
steps=args.step_size
hash_input=str(datetime.now()).encode('utf-8')
test_id=str(metrohash.metrohash64(hash_input).hex())



current_dir = os.getcwd()
filename='perfcheck.py'
file_loc = current_dir+'/'+filename
print(file_loc)
make_dir=["mkdir",f"{test_id}"]
subprocess.run(make_dir)
for num_user in range(args.lower_bound_users,args.upper_bound_users+1,args.step_size):
    write_config(test_id,num_user)
    rate=int(num_user*0.2)
    time=args.run_time_script #seconds
    locust_cmd=["locust","-f","/home/mihawk/thesis/locust_file/perfcheck.py",\
        "--headless","-u",f"{num_user}","-r",f"{rate}","-t",f"{time}",\
            "--csv-full-history",f"--csv={test_id}/{num_user}"]
    subprocess.run(locust_cmd)

logHost="10.129.7.11"
numLinesExtract=100000 # change this in the future
clientRun(test_id,logHost,numLinesExtract)

# for num_user in range(args.lower_bound_users,args.upper_bound_users+1,args.step_size):
#     pass
#locust -f perfcheck.py --headless -u 20 -r 2 -t 10