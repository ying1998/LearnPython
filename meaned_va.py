import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# csv_file_path = input("csv need to be processed such as ttvv_meaned_100k.csv :")
csv_file_path = "meaned_million_speed_25.csv"
df = pd.read_csv(csv_file_path)
title = "i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
title_maybe = "speed_ID,processed_speed,Unnamed: 0,i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
processed_speed = df['processed_speed']
DriverrID = df['DriverrID']
OrderID = df['OrderID']
Time_data= df['Time']
count = 0
i = 0
len_data = len(DriverrID)+1

def acceleration_data(v1,v2,i):
    a =  (v2 - v1) / (Time_data[i+1] -Time_data[i])
    return a



def processed_meaned_data(i,count):
    v1 = processed_speed[i]
    v2 = processed_speed[i+1]
    processed_a =acceleration_data(v1,v2,i)
    string_data = str(DriverrID[i])+","+str(OrderID[i])+","+str(processed_speed[i])+","+str(processed_a)+","+str(Time_data[i])+","+str(count)
    return string_data




with open('meaned_va_million.csv','r+') as file:
    file.write("DriverrID,OrderID,p_speed,p_a,Time,count\n")
    while i <= len_data and i+2 <= len_data:
        if OrderID[i] == OrderID[i+2]:
            file.write(str(processed_meaned_data(i,count))+"\n")
            i = i + 1
        else :
            i = i + 2
            count = count + 1
