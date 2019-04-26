#encoding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import sklearn.cluster as skc  # 密度聚类
from sklearn import metrics   # 评估模型
from sklearn.cluster import KMeans
#定义x、y散点坐标
df = pd.read_csv("list_va_million.csv")
speed_data = df['speed']
acceleration = df['acceleration']
# list1 = speed_data[0:15]
# list2 = acceleration[0:15]
list_speed = speed_data.values.tolist()
list_acceleration = acceleration.values.tolist()

def get_data(number):
    if 1 <= number*15 < len(speed_data):
        x = list_speed[(number-1)*15:number*15]
        y = list_acceleration[(number-1)*15:number*15]
    return x,y
number = 1
# dbscan = np.array([0,0,0,0])
list_dbscan = []
list_a = []
list_b = []
list_c = []
list_d = []
while number < len(speed_data)/15:
    x,y = get_data(number)
    f1 = np.polyfit(x, y, 3)
    a,b,c,d = f1
    list1 = [a,b,c,d]
    list_a.append(a)
    list_b.append(b)
    list_c.append(c)
    list_d.append(d)
    list_dbscan.append(list1)
    #dbscan = np.vstack((dbscan,f1))
    p1 = np.poly1d(f1)
    number = number + 1



#print(dbscan)
# print(list_dbscan)
list_a_sorted = sorted(list_a)
list_b_sorted = sorted(list_b)
list_c_sorted = sorted(list_c)
list_d_sorted = sorted(list_d)
def Normalized_abcd(list_a,list_a_sorted):
    a_max = list_a_sorted[-1]
    a_min = list_a_sorted[0]
    list_a_Normalized = []
    i = 0
    while i < len(list_a):
        list_a_Normalized.append((list_a[i] - a_min) / (a_max - a_min))
        i = i + 1
    return list_a_Normalized

list_a_Normalized = Normalized_abcd(list_a,list_a_sorted)
list_b_Normalized = Normalized_abcd(list_b,list_b_sorted)
list_c_Normalized = Normalized_abcd(list_c,list_c_sorted)
list_d_Normalized = Normalized_abcd(list_d,list_d_sorted)

def sum_abcd(a,b,c,d):
    i = 0
    list_dbscan_Normalized = []
    while i < len(a):
        list_dbscan_Normalized.append([a[i],b[i],c[i],d[i]])
        i = i + 1
    return list_dbscan_Normalized
list_dbscan_Normalized = sum_abcd(list_a_Normalized,list_b_Normalized,list_c_Normalized,list_d_Normalized)

data = list_dbscan_Normalized

# print(data[0])
# def distance_x1_x2(x,y):
#     pingfang = (data[x][0]-data[y][0])**2 + (data[x][1]-data[y][1])**2 + (data[x][2]-data[y][2])**2 + (data[x][3]-data[y][3])**2
#     distance  = math.sqrt(pingfang)
#     return distance

# distance1 = distance_x1_x2(2,3)
# distance2 = distance_x1_x2(3,4)
# distance3 = distance_x1_x2(5,2)
#
# j = 0
# while j < len(data):
#     k = 0
#     while k < len(data):
#         distance_j_k = distance_x1_x2(j,k)
#         print(j,k,"distance_j_k = ",distance_j_k)
#         k = k + 1
#     j = j + 1




print(len(data))
X = np.array(data)
# eps should <= 0.15 and >= 0.005
db = skc.DBSCAN(eps=0.03, min_samples=3).fit(X) #DBSCAN聚类方法 还有参数，matric = ""距离计算方法
labels = db.labels_  #和X同一个维度，labels对应索引序号的值 为她所在簇的序号。若簇编号为-1，表示为噪声

print('每个样本的簇标号:')
print(labels)

raito = len(labels[labels[:] == -1]) / len(labels)  #计算噪声点个数占总数的比例
print('噪声比:', format(raito, '.2%'))

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # 获取分簇的数目

print('分簇的数目: %d' % n_clusters_)
print("轮廓系数: %0.3f" % metrics.silhouette_score(X, labels)) #轮廓系数评价聚类的好坏
# k-means_data
for i in range(n_clusters_):
    print('簇 ', i, '的所有样本:')
    one_cluster = X[labels == i]
    if i == 0 :
        k_means_data = one_cluster.tolist()
        # print("k_means   -------------------")
        # print(k_means_data)
    print(one_cluster)
    plt.plot(one_cluster[:,0],one_cluster[:,1],'o')

# plt.show()



kmeans = KMeans(n_clusters=1, random_state=0).fit(k_means_data)
print("kmeans.cluster_centers")
print(kmeans.cluster_centers_)
center_a = kmeans.cluster_centers_[0][0]
center_b = kmeans.cluster_centers_[0][1]
center_c = kmeans.cluster_centers_[0][2]
center_d = kmeans.cluster_centers_[0][3]
def Back_Normalized_abcd(center_a,list_a_sorted):
    a_max = list_a_sorted[-1]
    a_min = list_a_sorted[0]
    b_center_a = center_a * (a_max - a_min) + a_min
    return b_center_a
p_center_a = Back_Normalized_abcd(center_a,list_a_sorted)
p_center_b = Back_Normalized_abcd(center_b,list_b_sorted)
p_center_c = Back_Normalized_abcd(center_c,list_c_sorted)
p_center_d = Back_Normalized_abcd(center_d,list_d_sorted)

f2 =  np.array([p_center_a,p_center_b,p_center_c,p_center_d])
print(f2)
p2 = np.poly1d(f2)
yvals = p2(x)
# plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('v m/s')
plt.ylabel('a m/s^2')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()


