import numpy as np
import pandas as pd
import matplotlib.pyplot as plt






title = "i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
print(title)
#csv_file_path=input("input csv file name :")
#csv_file_path = input("file name :")
csv_file_path = "corrected100kdata.csv"
df = pd.read_csv(csv_file_path)
one_data = input("x label = ")
two_data = input("y label = ")
DriverrID = df['DriverrID']
# speed_data = df['speed']
# time_data  = df['Time']
# count_data = df['count']
# i_data = df['i_ID']
# lendata = len(speed_data)
i = int(input("the dirver's local number is = "))
j = 0
while j < i and j < 100000 :
    if DriverrID[j] == DriverrID[i]:
        j = j + 100
    else:
        break
i = j
plt.figure()
plt.scatter(df[DriverrID[i],[one_data]],abs(df[DriverrID[i],[two_data]]))
plt.show()
