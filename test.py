import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#
# i = 10000
# j = 0
# while j < i and j < 100000 :
#     if j < i:
#         j = j + 100
#     else:
#         break
#         j = j + 101
#     print("the number is "+str(j))
title = "i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
print(title)
#csv_file_path=input("input csv file name :")
#csv_file_path = input("file name :")
csv_file_path = "corrected100kdata.csv"
df = pd.read_csv(csv_file_path)
DriverrID = df['DriverrID']

def set_local(i):
    j = 0
    while j < 100000 :
        if DriverrID[j] != DriverrID[i]:
            j = j + 100
        else:
            x = j
            y = j
            while DriverrID[x]== DriverrID[x+1] and x > 0:
                x = x - 1  # DriverrID begin
            while DriverrID[y]== DriverrID[y+1] and y <100000:
                y = y + 1  #DriverrID last
            break
    return x,y

def main_plot(arg):
    pass
soon = int(input("the dirver's local number is = "))
while True:
    x , y=set_local(soon)
    plt.figure()
    plt.scatter(df.loc[x:y,['speed']],abs(df.loc[x:y,['acceleration']]))
    plt.show()
    soon = int(input("the dirver's local number is = "))
    if soon != 0 :
        continue
    else:
        break



# plt.figure()
# plt.scatter(df.loc[x:y,['speed']],abs(df.loc[x:y,['acceleration']]),s=1)
# plt.show()
