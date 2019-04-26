#encoding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#定义x、y散点坐标

# print(list1)

x = [0.8358562480902941, 1.957784361810572, 2.1504834538209976, 3.135751538097859, 4.085436873894045, 5.6565839992983, 6.189965330408128, 7.567196047108491, 8.201546511766526, 9.351740878301001, 10.089047226132882, 11.121618325299439, 12.907953018925483, 13.349085289978149, 14.175784740106222]


y = [0.20157466794985546, 0.5435544429768328, 0.6203615133028703, 0.6676140826765273, 0.623936276000914, 0.6883179033520221, 0.6741025376644263, 0.7418819654027929, 0.78015793726521, 0.7296097539098412, 0.8311434992424088, 0.9282619298575648, 0.8715087006195308, 1.0960459509773912, 0.9254606448554772]


#用3次多项式拟合
f1 = np.polyfit(x, y, 3)
print(f1)
print(f1.dtype)
a,b,c,d = f1
array_abcd = np.array([a,b,c,d])
print(array_abcd)
print(a,b,c,d)
p1 = np.poly1d(f1)
print(p1)

#也可使用yvals=np.polyval(f1, x)
yvals = p1(x)  #拟合y值

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('v m/s')
plt.ylabel('a m/s^2')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()
# plt.savefig('test.png')
# ---------------------
# 作者：Eastmount
# 来源：CSDN
# 原文：https://blog.csdn.net/eastmount/article/details/71308373
# 版权声明：本文为博主原创文章，转载请附上博文链接！
