import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def mean5_3(Series,m):
    n=len(Series)
    a=Series
    b=Series.copy()
    for i in range(m):
        b[0] = (69*a[0] + 4*(a[1] + a[3]) - 6*a[2] - a[4]) /70
        b[1] = (2*(a[0] + a[4]) +27*a[1] + 12*a[2] - 8*a[3]) /35
        for j in range(2,n-2):
            b[j] = (-3*(a[j-2] + a[j+2]) + 12*(a[j-1] + a[j+1]) + 17*a[j]) /35
        b[n-2] = (2*(a[n-1] + a[n-5]) + 27*a[n-2] + 12*a[n-3] - 8*a[n-4]) /35
        b[n-1] = (69*a[n-1] + 4*(a[n-2] + a[n-4]) - 6*a[n-3] -a[n-5]) /70
        a=b.copy()
    return a


# csv_file_path = input("csv need to be processed such as right100kdata_speed_25.csv :")
csv_file_path = 'right_million_speed_25.csv'
df = pd.read_csv(csv_file_path)
title = "i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"

# DriverrID = df['DriverrID']
# OrderID   = df['OrderID']

mean5_3time = pd.Series(df['speed'])
processed_data = abs(mean5_3(mean5_3time,1))
df.insert(0,column="processed_speed",value = processed_data)
df.to_csv('meaned_million_speed_25.csv')
