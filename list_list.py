import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



list_1 = [1,2,5,9,0,7]
list_2 = ['1','3','2']
list_3 = ['3']
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
# list_1.sort(reverse=True)
# print(list_1)
list_list[0].sort()
print(list_list[0])
list_5.sort()
print(len(list_5))
df = pd.read_csv("meaned_va.csv")
title = "DriverrID,OrderID,p_speed,p_a,Time,count"
print(title)

DriverrID = df['DriverrID']
p_speed = df['p_speed']
p_a     = df['p_a']
long =len(DriverrID)
# if p_speed[2] < 2.0:
#     print(p_speed[2])
print(p_speed[2].dtype)

#
# print(list_2.sort())
