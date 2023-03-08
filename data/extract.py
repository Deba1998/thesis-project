import re
def extract_time(id_pattern,file_name):
    only_id_pattern=re.compile(id_pattern)
    id_pattern="/"+id_pattern+"/"+"[0-9]+"
    num_users_pattern = re.compile(id_pattern)
    response_time_pattern = re.compile("\*\*\*.*\*\*\*")
    current_users=-1
    with open(file_name) as file_h:
        count=0
        time=0
        for line in file_h:
            try:
                if line.strip()!="":
                    users=int(num_users_pattern.search(line).group(0)[18:])
                    if current_users==-1:
                        current_users=users
                    if current_users!=users:
                        avg_time=time/count
                        print(str(current_users)+","+str(avg_time))
                        current_users=users
                        count=0
                        time=0
                    response_time=float(response_time_pattern.search(line).group(0)[3:][:-3])
                    count+=1
                    time+=response_time
            except AttributeError :
                if only_id_pattern.search(line) == None:
                    print(line)
                    print("AttributeError")
                    exit(1)
        avg_time=time/count
        print(current_users,avg_time)

# file_lst=["inner-nginx-1a1b1bb9ae239420.log","outer-nginx-1a1b1bb9ae239420.log","uwsgi-1a1b1bb9ae239420.log"]
file_lst=[
"inner-nginx-cb20c93946537c12.log",
"outer-nginx-cb20c93946537c12.log",
"uwsgi-cb20c93946537c12.log"
]
for file in file_lst:
    id_pattern='cb20c93946537c12'
    print(file)
    extract_time(id_pattern,file)