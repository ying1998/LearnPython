import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

csv_file_path='million.csv'
order_file = './order_20161101'
# df = pd.read_csv(csv_file_path)
order_info = pd.read_csv(order_file, infer_datetime_format=True,\
                            header=None, parse_dates = [1],\
                            names = ['order_id', 'start_time', 'end_time','boarding_long','boarding_grat','depature_long','depature_grat'])


print ('Size of data frame: ', order_info.shape)
# print(order_info)
# print(order_info.describe())
order_info.drop_duplicates(inplace=True)
order_info.dropna(inplace=True)
print ('Size of data frame: ', order_info.shape)
print ("Plotting position density...")
# xmin, xmax =  29.51 , 31.33
# ymin, ymax = 103.25,  104.70
xmin, xmax = 30.65, 30.72
ymin, ymax = 104.042, 104.129

plt.figure(figsize = (20,10), dpi=500)
plt.hexbin(order_info['boarding_grat'][:10000],order_info['boarding_long'][:10000], bins='log', gridsize=1000, cmap=plt.cm.hot)
plt.axis([xmin, xmax, ymin, ymax])
plt.title("Traffic data: overview")
plt.xlabel('Longitude (degrees)')
plt.ylabel('Latitude (degrees)')

# cb = plt.colorbar(format=LogFormatterHB())
# cb.set_label('Number of points')

# plt.savefig("filename.png")

plt.tight_layout()
plt.show()
