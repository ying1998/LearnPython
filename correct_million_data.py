import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

title = "i_ID,DriverrID,OrderID,distance,speed,acceleration,count,Time\n"
print(title)
#csv_file_path=input("input csv file name :")
csv_file_path = "million_processed_data.csv"
df = pd.read_csv(csv_file_path)
speed_data = df['speed']
count_data_1 = 0
count_data_2 = 0
i = 0
long = len(speed_data) - 1
speed_lower_15 = df[df.speed<25]
speed_lower_15.to_csv('right_million_speed_25.csv')
