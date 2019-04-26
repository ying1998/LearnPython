import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
title = "i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
print(title)
title_maybe = "speed_ID,processed_speed,Unnamed: 0,i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
print(title_maybe)
#csv_file_path=input("input csv file name :")
# csv_file_path = input("file name :")
csv_file_path = "meaned_va_million.csv"
df = pd.read_csv(csv_file_path)
one_data = input("x label = ")
two_data = input("y label = ")
DriverrID = df['DriverrID']
OrderID   = df['OrderID']
long = len(DriverrID)
def DriverrID_set_local(i):
    j = 0
    while j < long :
        if DriverrID[j] != DriverrID[i]:
            j = j + 100
        else:
            x = j
            y = j
            while DriverrID[x]== DriverrID[x+1] and x > 0:
                x = x - 1  # DriverrID begin
            while DriverrID[y]== DriverrID[y+1] and y <long:
                y = y + 1  #DriverrID last
                if y == long - 1 :
                    break
            break
    return x+1,y

def OrderID_set_local(i):
    j = 0
    while j < long :
        if OrderID[j] != OrderID[i]:
            j = i
        else:
            x = j
            y = j
            while OrderID[x]== OrderID[x+1] and x > 0:
                x = x - 1  # DriverrID begin
            while OrderID[y]== OrderID[y+1] and y <long:
                y = y + 1  #DriverrID last
                if y == long-1:
                    break
            break
    return x+1,y

def count_driver_number():
    j_number = 0
    i = 0
    driverIDnumber=[]
    while i <= long and (i+100) <=long:
        if DriverrID[i] == DriverrID[i+100]:
            i = i + 100
        else:
            j_number = j_number + 1
            i = i + 100
            driverIDnumber.append(i)

    return j_number,driverIDnumber

def count_order_number(i):
    x,y = DriverrID_set_local(i)
    j_number = 0
    OrderIDnumber=[]
    while x<= i and i + 1 <= y :
        if OrderID[i] == OrderID[i+1]:
            i = i + 1
        else:
            j_number = j_number + 1
            i = i + 1
            OrderIDnumber.append(i)
    return j_number,OrderIDnumber

# speed_data = df['speed']
# time_data  = df['Time']
# count_data = df['count']
# i_data = df['i_ID']
# lendata = len(speed_data)
# i = int(input("the dirver's local number is = "))
Drivernumber,DriverIDstation=count_driver_number()
print("the number of driver is =",Drivernumber)
print("the station of each driver is =",DriverIDstation)
DriverrID_soon = int(input("the driver's local number you want is = "))
# driver_x,driver_y = DriverrID_set_local(DriverrID_soon)
# print("the number of order is =",Ordernumber)
# print("the station of each order is =",OrderIDstation)
# OrderID_soon   = int(input("the OrderID number you want is ="))
# order_x,order_y=OrderID_set_local(OrderID_soon)



while True:
    Ordernumber,OrderIDstation=count_order_number(DriverrID_soon)
    print("the number of order is =",Ordernumber)
    print("the station of each order is =",OrderIDstation)
    OrderID_soon   = int(input("the OrderID number you want is ="))
    order_x,order_y=OrderID_set_local(OrderID_soon)
    x = order_x
    y = order_y
    plt.figure()
    #plt.scatter(df.loc[x:y,[one_data]],abs(df.loc[x:y,[two_data]]))
    plt.plot(df.loc[x:y,[one_data]],df.loc[x:y,[two_data]])
    plt.show()
    DriverrID_soon = int(input("the dirver's local number is = "))
    if DriverrID_soon != 0 :
        continue
    else:
        break











# plt.figure()
# #plt.xlim(0.5, 5.5) show the area of x
# #plt.ylim(0.5, 1.0) show y
# # plt.xlim(1477983977, 1477984905)
# # plt.ylim(0, 40)
# #plt.scatter(df[one_data],abs(df[two_data]))
# plt.scatter(df.loc[driver_x:driver_y,[one_data]],abs(df.loc[driver_x:driver_y,[two_data]]))
# plt.show()
