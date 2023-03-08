import csv
import os 

def extract_data(test_id,num_users):
    path = os.getcwd()+"/"+test_id+"/"+str(num_users)+"_stats_history.csv"
    file = open(path,newline='')
    reader = csv.reader (file)

    header = next(reader)
    print(header)
    count=0
    for item in header:
        if item=="Total Average Response Time":
            break
        count+=1
    data = 1
    while data:
        data = next(reader)
        print(data[count])
    pass
extract_data("70c35d6f6ef367db",20)