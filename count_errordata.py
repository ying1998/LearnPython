import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

title = "i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
print(title)
#csv_file_path=input("input csv file name :")
csv_file_path = "3000data.csv"
df = pd.read_csv(csv_file_path)
speed_data = df['speed']
count_data_1 = 0
count_data_2 = 0
i = 0
long = len(speed_data) - 1

with open('revise_3000.csv','r+') as file:
    file.write("i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n")
    while i <= long:
        if speed_data[i] > 15.0:
            count_data_1= count_data_1 + 1
            i = i + 1
        else:
            whole_data =
            file.write()
            count_data_2 = count_data_2 + 1
            i = i + 1
            pass
            
while i <= long:
    if speed_data[i] > 15.0:
        count_data_1= count_data_1 + 1
        i = i + 1
    else:
        count_data_2 = count_data_2 + 1
        i = i + 1
        pass

print("there is "+str(count_data_1)+ "  faster than 15m/s ")
print("there is "+str(count_data_2)+ "  slower than 15m/s ")
#print(speed_data)
