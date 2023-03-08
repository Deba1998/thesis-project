import pandas as pd
import matplotlib.pyplot as plt
import json
#test_id="cb20c93946537c12"
def showGraph(test_id):
    file_lst=[]
    y_list=[]
    components=[]
    f = open('components.json')
    data = json.load(f)
    for i in data:
        res=i["componentName"]+"-"+test_id+".csv"
        file_lst.append(res)
        y_list.append("y_"+i["componentName"])
        components.append(i["componentName"])
    # Closing file
    f.close()
    for i in range(len(file_lst)):
        var=pd.read_csv(file_lst[i])
        y_list[i]=list(var['Averagetime'])
    
    for p in y_list:
        p.insert(0,0)

    x = list(var['Numusers'])
    x.insert(0,0)

    for i in range(len(y_list)):
        plt.plot(x,y_list[i],label=components[i])

    plt.legend(loc='best')
    plt.show()


# var3 = pd.read_csv("inner-nginx-cb20c93946537c12.csv")
# var1 = pd.read_csv("outer-nginx-cb20c93946537c12.csv")
# var2 = pd.read_csv("uwsgi-cb20c93946537c12.csv")

# x = list(var2['Numusers'])
# y_uwsgi = list(var2['Averagetime'])
# y_inner=  list(var3['Averagetime'])
# y_outer=  list(var1['Averagetime'])
# x.insert(0,0)
# y_inner.insert(0,0)
# y_outer.insert(0,0)
# y_uwsgi.insert(0,0)

# import matplotlib.pyplot as plt
# plt.plot(x,y_uwsgi,color='r',label='uwsgi')
# plt.plot(x,y_inner,color='b',label='inner-nginx')
# plt.plot(x,y_outer,color='g',label='outer-nginx')
# plt.xlabel("Num of users")
# plt.ylabel("Response time")
# plt.title("performance of different backend components")
# plt.legend()
# plt.show()

# x = np.linspace(0, 1, 10)
# for i in range(1, 6):
#     plt.plot(x, i * x + i, label='$y = {i}x + {i}$'.format(i=i))
# plt.legend(loc='best')
# plt.show()