import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = ['a', 'b', 'c', 'd', 'e', 'f']
# c = list(zip(list1,list2))
# print(c)
# print("-------------------")
# c.sort(reverse = True) #降序
# list1[:],list2[:] = zip(*c)
# print(list1,list2)


#-------------------------------
df = pd.read_csv("meaned_va_million.csv")
title = "DriverrID,OrderID,p_speed,p_a,Time,count"
print(title)

DriverrID = df['DriverrID']
p_speed = df['p_speed']
p_a     = df['p_a']
long =len(DriverrID)








def sort_va(p_speed,p_a,driver_x,driver_y):
    list1 = df.loc[driver_x:driver_y,['p_speed']].values.tolist()
    # print(list1)
    list2 = abs(df.loc[driver_x:driver_y,['p_a']].values).tolist()
    c = list(zip(list1,list2))
    c.sort(reverse = True)
    processed_speed=[]
    processed_acceleration = []
    processed_speed[:],processed_acceleration[:] = zip(*c)
    # va = pd.DataFrame({'speed':pd.Series(list1),
    #                 'acceleration':pd.Series(list2)
    # })
    # # processed_speed = va['speed']
    # processed_acceleration = va['acceleration']
    select_value_a=[]
    select_value_v=[]
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    list_9 = []
    list_10 = []
    list_11 = []
    list_12 = []
    list_13 = []
    list_14 = []
    list_15 = []
    list_list = [list_1,list_2,list_3,list_4,list_5,list_6,list_7,list_8,list_9,list_10,list_11,list_12,list_13,list_14,list_15]
    i = 0
    # print(processed_speed[0][0])
    # print(processed_acceleration[0][0])
    while i < len(processed_speed):
        if 0 < processed_speed[i][0] <= 1:
            list_1.append(processed_acceleration[i][0])
        elif 1.0 < processed_speed[i][0] <= 2.0:
            list_2.append(processed_acceleration[i][0])
        elif 2.0 < processed_speed[i][0] <= 3.0:
            list_3.append(processed_acceleration[i][0])
        elif 3.0 < processed_speed[i][0] <= 4.0:
            list_4.append(processed_acceleration[i][0])
        elif 4.0 < processed_speed[i][0] <= 5.0:
            list_5.append(processed_acceleration[i][0])
        elif 5.0 < processed_speed[i][0] <= 6.0:
            list_6.append(processed_acceleration[i][0])
        elif 6.0 < processed_speed[i][0] <= 7.0:
            list_7.append(processed_acceleration[i][0])
        elif 7 < processed_speed[i][0] <= 8.0:
            list_8.append(processed_acceleration[i][0])
        elif 8 < processed_speed[i][0] <= 9.0:
            list_9.append(processed_acceleration[i][0])
        elif 9 < processed_speed[i][0] <= 10.0:
            list_10.append(processed_acceleration[i][0])
        elif 10 < processed_speed[i][0] <= 11.0:
            list_11.append(processed_acceleration[i][0])
        elif 11 < processed_speed[i][0] <= 12.0:
            list_12.append(processed_acceleration[i][0])
        elif 12 < processed_speed[i][0] <= 13.0:
            list_13.append(processed_acceleration[i][0])
        elif 13 < processed_speed[i][0] <= 14.0:
            list_14.append(processed_acceleration[i][0])
        elif 14 < processed_speed[i][0] <= 15.0:
            list_15.append(processed_acceleration[i][0])
        i = i + 1
    j = 0
    while j < 15 :
        list_list[j].sort()
        list_long = len(list_list[j])
        select_number = int(list_long*0.8)
        if select_number == 0:
            select_value = 0
            if  j > 0 :
                print("too little data ")
                select_value = select_value_a[j-1]
        else:
            select_value = list_list[j][select_number]
            if select_value == 0 :
                select_value = list_list[j][select_number+1]
                if select_value  == 0 and j > 0 :
                    print("too little data ")
                    select_value = select_value_a[j-1]
        # if select_value == 0 :
        #     select_value = list_list[j][select_number+1]
        #     if select_value  == 0 and j > 0 :
        #         print("too little data ")
        #         select_value = select_value_a[j-1]
        select_value_a.append(select_value)
        k = 0
        while k < len(processed_acceleration):
            if processed_acceleration[k][0] == select_value :
                select_value_speed=processed_speed[k][0]
                select_value_v.append(select_value_speed)
                break #x and y must be the same size
            k = k + 1
        j = j + 1

    return select_value_v,select_value_a



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
                if y == long -1 :
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
                if y == long -1 :
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




Drivernumber,DriverIDstation=count_driver_number()
print("the number of driver is =",Drivernumber)
print("the station of each driver is =",DriverIDstation)
DriverrID_soon = int(input("the driver's local number you want is = "))
driver_x,driver_y = DriverrID_set_local(DriverrID_soon)


while True:
    driver_x , driver_y=DriverrID_set_local(DriverrID_soon)
    # plt.figure()
    # plt.scatter(df.loc[x:y,[one_data]],abs(df.loc[x:y,[two_data]]))
    # plt.show()
    list1 ,list2 = sort_va(p_speed,p_a,driver_x,driver_y)
    print(list1)
    print("------------------")
    print(list2)
    plt.figure()
    
    plot2 = plt.scatter(df.loc[driver_x:driver_y,['p_speed']],abs(df.loc[driver_x:driver_y,['p_a']]))
    plt.scatter(list1,list2,c='r')
    plt.show()
    DriverrID_soon = int(input("the dirver's local number is = "))
    if DriverrID_soon != 0 :
        continue
    else:
        break
