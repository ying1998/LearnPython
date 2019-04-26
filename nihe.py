#encoding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#定义x、y散点坐标
df = pd.read_csv("list_va_million.csv")
speed_data = df['speed']
acceleration = df['acceleration']
# list1 = speed_data[0:15]
# list2 = acceleration[0:15]
list_v = speed_data.values.tolist()
list_a = acceleration.values.tolist()

while True:
    number = int(input("choose your number : ----<=:"+str(len(speed_data)/15)+"----->"))
    if 1 <= number*15 < len(speed_data):
        x = list_v[(number-1)*15:number*15]
        y = list_a[(number-1)*15:number*15]
    elif number == 0:
        break
    else:
        print("please input right 0 < number <98")
    f1 = np.polyfit(x, y, 3)
    p1 = np.poly1d(f1)
    print(p1)

    #也可使用yvals=np.polyval(f1, x)
    yvals = p1(x)  #拟合y值
    print(yvals)
    #绘图
    plot1 = plt.plot(x, y, 's',label='original values')
    plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4) #指定legend的位置右下角
    plt.title('polyfitting')
    plt.show()
