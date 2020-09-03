import pandas as pd
import numpy as np
import random

simulation = 2000
lam_customer = 5 #per Hour
lam_server1 = 3 #per Hour
lam_server2 = 4 #per Hour
time_c = 0
time_1 = 0 # the time when server1's last job ends
time_2 = 0 # the time when server2's last job ends

n = 0


len_queue_1 = []
len_queue_2 = []
queue_1 = []
queue_2 = []


df_server_1 = pd.DataFrame({"Customer" : [], "Arrival Time" : [], "Service Start Time" : []
                        ,"Service Time" : [], "Service End Time" : [], "W_q1" : []})
df_server_2 = pd.DataFrame({"Customer" : [], "Arrival Time" : [], "Service Start Time" : []
                        ,"Service Time" : [], "Service End Time" : [], "W_q2" : []})

def customerArrival():
    return np.random.exponential(scale = 1/lam_customer)
def serverFunc_1():
    return np.random.exponential(scale = 1/lam_server1)
def serverFunc_2():
    return np.random.exponential(scale = 1/lam_server2)



def server_1(x): # the present time : x
    global time_1 # the time when server1's last job ends
    while True:
        if len(queue_1) == 0:
            break
        if time_1 > x:
            break
        

        operationTime = serverFunc_1()
        df_server_1.loc[len(df_server_1),["Customer","Arrival Time","Service Time"]] = [queue_1[0][0],queue_1[0][1],operationTime]
        if queue_1[0][1] >= time_1:
            wq = 0
            startTime = queue_1[0][1]
            time_1 = startTime + operationTime
            df_server_1.loc[len(df_server_1) - 1,["Service Start Time","Service End Time","W_q1"]] = [startTime, time_1, wq]
        elif queue_1[0][1] < time_1:
            wq = time_1 - queue_1[0][1]
            startTime = time_1
            time_1 += operationTime
            df_server_1.loc[len(df_server_1) - 1,["Service Start Time","Service End Time","W_q1"]] = [startTime, time_1, wq]
        del queue_1[0]
        
        
        
    
    
def server_2(x):# the present time : x
    global time_2 # the time when server2's last job ends
    while True:
        if len(queue_2) == 0:
            break
        if time_2 > x:
            break
        

        operationTime = serverFunc_2()
        df_server_2.loc[len(df_server_2),["Customer","Arrival Time","Service Time"]] = [queue_2[0][0],queue_2[0][1],operationTime]
        if queue_2[0][1] >= time_2:
            wq = 0
            startTime = queue_2[0][1]
            time_2 = startTime + operationTime
            df_server_2.loc[len(df_server_2) - 1,["Service Start Time","Service End Time","W_q2"]] = [startTime, time_2, wq]
        elif queue_2[0][1] < time_2:
            wq = time_2 - queue_2[0][1]
            startTime = time_2
            time_2 += operationTime
            df_server_2.loc[len(df_server_2) - 1,["Service Start Time","Service End Time","W_q2"]] = [startTime, time_2, wq]
        del queue_2[0]
  

while True:
    time_c += customerArrival()
    server_1(time_c)
    server_2(time_c)
  
    if len(queue_1) == len(queue_2):
        if random.randint(0,10)%2 == 0:
            len_queue_1.append([len(queue_1),n])
            queue_1.append([n, time_c])
        else:
            len_queue_2.append([len(queue_2),n])
            queue_2.append([n, time_c])
    elif len(queue_1) > len(queue_2):
        len_queue_2.append([len(queue_2),n])
        queue_2.append([n, time_c])
    elif len(queue_1) < len(queue_2):
        len_queue_1.append([len(queue_1),n])
        queue_1.append([n, time_c])
    
    n += 1
    if n == simulation:
        break
    else:
        continue
    
    
time_c += 100
server_1(time_c)
server_2(time_c)

print(" ")
print("▼▼▼▼▼ Average wating time on queue ▼▼▼▼▼")    
print("W_q1 =",df_server_1.loc[0:len(df_server_1),"W_q1"].mean()*60,"(minutes)")
print("W_q2 =",df_server_2.loc[0:len(df_server_2),"W_q2"].mean()*60,"(minutes)")   
print(" ")
print("▼▼▼▼▼ Average length of queue when a new customer arrives ▼▼▼▼▼")
print("L_q1 =",sum(len_queue_1[i][0] for i in range(len(len_queue_1)))/len(len_queue_1))  
print("L_q2 =",sum(len_queue_2[i][0] for i in range(len(len_queue_2)))/len(len_queue_2))
print("\n ##################################################\n ########### Coded by 15113369 HONG.S.R ###########\n",
      "##################################################")