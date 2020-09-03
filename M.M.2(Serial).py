import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

simulation = 5000
lam_customer = 5 #per Hour
lam_server1 = 8 #per Hour
lam_server2 = 6 #per Hour
time_1 = 0
time_2 = 0
n = 0


customerDist = pd.DataFrame({"Customer" : [],"Inter Arrival Time" : [], "Arrival Time" : []})
queue_1 = pd.DataFrame({"Customer" : [], "Arrival Time" : [], "Service Start Time" : []
                        ,"Service Time" : [], "Service End Time" : [], "W_q1" : []})
queue_2 = pd.DataFrame({"Customer" : [], "Arrival Time" : [], "Service Start Time" : []
                        ,"Service Time" : [], "Service End Time" : [], "W_q2" : []})

def customerArrival():
    return np.random.exponential(scale = 1/lam_customer)
def server_1():
    return np.random.exponential(scale = 1/lam_server1)
def server_2():
    return np.random.exponential(scale = 1/lam_server2)

# Defines customer table
while True:
    h = customerArrival()
    time_1 += h
    customerDist.loc[n,["Customer","Inter Arrival Time","Arrival Time"]] = [n, h,time_1]
    if n == simulation - 1:
        n = 0
        time_1 = 0
        break
    else:
        n += 1
        continue


# Defines queue_1 table
while True:
    if n == simulation:
        n = 0
        break
   
    queue_1.loc[n,["Customer","Arrival Time","Service Time"]] = [n,customerDist.loc[n,"Arrival Time"],server_1()]
    if time_1 <= queue_1.loc[n,"Arrival Time"]:
        queue_1.loc[n,["Service Start Time","W_q1"]] = [queue_1.loc[n,"Arrival Time"], 0]
        queue_1.loc[n,"Service End Time"] = queue_1.loc[n,"Service Start Time"] + queue_1.loc[n,"Service Time"]
    elif time_1 > queue_1.loc[n,"Arrival Time"]:
        queue_1.loc[n,"Service Start Time"] = time_1
        queue_1.loc[n,"Service End Time"] = queue_1.loc[n,"Service Start Time"] + queue_1.loc[n,"Service Time"]
        queue_1.loc[n,"W_q1"] = queue_1.loc[n,"Service Start Time"] - queue_1.loc[n, "Arrival Time"]
    time_1 = queue_1.loc[n,"Service End Time"]
    
    n += 1
   
# Defines queue_2 table    
while True:
    if n == simulation:
        break
    queue_2.loc[n,["Customer","Service Time","Arrival Time"]] = [n, server_2() , queue_1.loc[n, "Service End Time"]]
    if time_2 <= queue_2.loc[n,"Arrival Time"]:
        queue_2.loc[n,["Service Start Time","W_q2"]] = [queue_2.loc[n,"Arrival Time"], 0]
        queue_2.loc[n,"Service End Time"] = queue_2.loc[n,"Service Start Time"] + queue_2.loc[n,"Service Time"]
    elif time_2 > queue_2.loc[n,"Arrival Time"]:
        queue_2.loc[n,"Service Start Time"] = time_2
        queue_2.loc[n,"Service End Time"] = queue_2.loc[n,"Service Start Time"] + queue_2.loc[n,"Service Time"]
        queue_2.loc[n,"W_q2"] = queue_2.loc[n,"Service Start Time"] - queue_2.loc[n, "Arrival Time"]
    time_2 = queue_2.loc[n,"Service End Time"]
     
    n += 1
    

# Result Output #
print(" ##################################################\n ########### Coded by 15113369 HONG.S.R ###########\n",
      "##################################################")
    
hist = plt.hist(customerDist.loc[0:simulation,"Inter Arrival Time"],edgecolor = 'black')
plt.xlabel("Inter Arrival Time(Hour)")
plt.ylabel("Frequency")
plt.title("Customer Distribution")
plt.show()

print(" ")    
print("W_q1 =",queue_1.loc[0:simulation,"W_q1"].mean()*60,"(minutes)")
print("W_q2 =",queue_2.loc[0:simulation,"W_q2"].mean()*60,"(minutes)")        
print("Total Average Wating Time =",(queue_1.loc[0:simulation,"W_q1"].mean()+queue_2.loc[0:simulation,"W_q2"].mean())*60,"(minutes)")

print(" ##################################################\n ########### Coded by 15113369 HONG.S.R ###########\n",
      "##################################################")