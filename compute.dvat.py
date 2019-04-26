import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def Longitute_gap(Longitute_data,i):
    ll_data = (Longitute_data[i+1] - Longitute_data[i])*math.pi/float(180)
    return ll_data

def haversin(x):
    x = (1-math.cos(x))/2
    return x
def distance_data(Latitude_data,i,ll_data):
    Latitude_local_1 = Latitude_data[i]*math.pi/float(180)
    Latitude_local_2 = Latitude_data[i+1]*math.pi/float(180)
    h = haversin(Latitude_local_1 - Latitude_local_2)+math.cos(Latitude_local_2)*math.cos(Latitude_local_1)*haversin(ll_data/2)
    d = 2*R*np.arcsin(math.sqrt(h))
    return d

def speed(d,i):
    v = d/(Time_data[i+1]-Time_data[i])
    return v

def speed_late(Longitute_data,Latitude_data,i):
    i = i + 1
    ll_data = Longitute_gap(Longitute_data,i)
    d = distance_data(Latitude_data,i,ll_data)
    v = speed(d,i)
    return v

def acceleration_data(v1,v2,i):
    a =  (v2 - v1) / (Time_data[i+1] -Time_data[i])
    return a

def process_data_distance(Longitute_data,Latitude_data,i,count):
    ll_data = Longitute_gap(Longitute_data,i)
    d = distance_data(Latitude_data,i,ll_data)
    v1 = speed(d,i) # this time speed
    v2 = speed_late(Longitute_data,Latitude_data,i)
    a = acceleration_data(v1,v2,i)
    i = i + 1
    ProcessedData = str(i)+","+str(DriverrID[i])+","+str(OrderID[i])+","+str(d)+","+str(v1)+","+str(a)+","+str(count)+","+str(Time_data[i])
    return ProcessedData







data = 'DriverrID,OrderID,Time,Longitute,Latitude'
csv_file_path='million.csv'
df = pd.read_csv(csv_file_path)
d = 0 # distance_data
R = 6371000  #the R of earth
Longitute_data = df['Longitute']
Latitude_data  = df['Latitude']
Time_data = df['Time']
DriverrID = df['DriverrID']
OrderID = df['OrderID']
Latitude_local_1 = 0 # 1 Latitude
Latitude_local_2 = 0 # 2 Latitude
i = 0
count = 0
len_data = len(Longitute_data)
with open('million_processed_data.csv','r+') as file:
    file.write("i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n")
    while i <= len_data and i+1 <= len_data:
        if OrderID[i] == OrderID[i+2]:
            file.write(str(process_data_distance(Longitute_data,Latitude_data,i,count))+"\n")
            i = i + 1
        else :
            i = i + 2
            count = count + 1
