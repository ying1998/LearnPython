#the same as select_va.py



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



def sort_va(p_speed,p_a,driver_x,driver_y,DriverrID_ID):
    list1 = df.loc[driver_x:driver_y,['p_speed']].values.tolist()
    # print(list1)
    list2 = abs(df.loc[driver_x:driver_y,['p_a']].values).tolist()
    c = list(zip(list1,list2))
    c.sort(reverse = True)
    if len(c) == 0 :
        print("c  is  null  -------- ")
        list1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        list2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        list_driverid = [DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID]
        return list1,list2,list_driverid
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
                print(driver_x+10)
                select_value = select_value_a[j-1]
                # 为了防止0-x m/s内有缺失数据
                if select_value_v[j-1]==0 and select_value_a[0]==0:
                    select_value_v.append(0)

            else:
                print("may be loss data ,the driver id is ",DriverrID_ID)
                print("we will set select_value = 0 ")
                select_value = 0
                select_value_v.append(0)
        else:
            select_value = list_list[j][select_number]
            if select_value == 0 :
                select_value = list_list[j][select_number+1]
                if select_value  == 0 and j > 0 :
                    print("too little data ")
                    print("----------",DriverrID_ID)
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
        long_v =len(select_value_v)
        long_a =len(select_value_a)
        list_driverid = [DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID,DriverrID_ID]
        if long_v != long_a:
            select_value_a.append(select_value_a[-1])
            break
        j = j + 1

    return select_value_v,select_value_a,list_driverid

def add_df_va(select_value_v,select_value_a,list_driverid):
    # print('speed',len(select_value_v))
    # print('acceleration',len(select_value_a))
    # print(list_driverid[0])
    df_list_va = pd.DataFrame({"speed" :select_value_v,
                        "acceleration":select_value_a,
                        "DriverrID":list_driverid[0]} )

    return df_list_va



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
            while DriverrID[y]== DriverrID[y+1] and y+1 <long:
                y = y + 1  #DriverrID last
                if y == long - 1 :
                    break
            break
    return x+1,y,DriverrID[y]

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
            while OrderID[y]== OrderID[y+1] and y+1 <long:
                y = y + 1  #DriverrID last
                if y == long - 1 :
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



df_list = pd.DataFrame({"speed" :0,
                        "acceleration":0,
                        "DriverrID":0},index=[0] )

Drivernumber,DriverIDstation=count_driver_number()
print("the number of driver is =",Drivernumber)
print("the station of each driver is =",DriverIDstation)
#DriverrID_soon = int(input("the driver's local number you want is = "))
#driver_x,driver_y,DriverrID_ID= DriverrID_set_local(DriverrID_soon)
l = 0

while l < len(DriverIDstation):
    driver_x,driver_y,DriverrID_ID= DriverrID_set_local(DriverIDstation[l])
    list1 ,list2,list_driverid = sort_va(p_speed,p_a,driver_x,driver_y,DriverrID_ID)
    df_list = df_list.append(add_df_va(list1,list2,list_driverid))
    l = l + 1

df_list.to_csv('list_va_100k.csv')



# while True:
#     driver_x,driver_y,DriverrID_ID=DriverrID_set_local(DriverrID_soon)
#     # plt.figure()
#     # plt.scatter(df.loc[x:y,[one_data]],abs(df.loc[x:y,[two_data]]))
#     # plt.show()
#     list1 ,list2,list_driverid = sort_va(p_speed,p_a,driver_x,driver_y,DriverrID_ID)
#     df_list.append(add_df_va(select_value_v,select_value_a,list_driverid))
#     # print(list1)
#     # print("------------------")
#     # print(list2)
#     # plt.figure()
#     # plt.scatter(list1,list2)
#     # plt.show()
#     #DriverrID_soon = int(input("the dirver's local number is = "))
#     if DriverrID_soon != 0 :
#         continue
#     else:
#         break
