#numpy读取数据和转置

import numpy as np

t1 = np.loadtxt("./youtube_video_data/US_video_data_numbers.csv",delimiter = ',',dtype = 'int')
print(t1)
print("--"*100)
#
#
# #转置
# t1 = np.loadtxt("./youtube_video_data/US_video_data_numbers.csv",delimiter = ',',dtype = 'int',unpack=True)
# print(t1)
#
# t2 = np.array([[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17]])
# print(t2)
# print(t2.transpose())
# print(t2.swapaxes(1,0))
# print(t2.T)

#取行
# print(t1[2])
# print(t1[2,:])

# 取连续的多行
# print(t1[2:])
# print(t1[2:,:])

#取不连续的多行
#print(t1[2,8,10])  -- 报错
# print(t1[[2,8,10]])
# print(t1[[2,8,10],:])

#取列
# print(t1[:,0])

#取连续的多列
# print(t1[:,2:])

#取不连续的多列
# print(t1[:,[0,2]])

#取行和列，取第三行，第四列的值
# print(t1[2,3])

#取多行和多列，取第3行到第5行，第2列到第4列的结果 -- 取的是行和列交叉点的位置
# print(t1[2:5,1:4])

#取多个不相邻的点
print(t1[[0,2],[0,1]])
print(t1[[0,2,1],[0,1,1]]) # 选出来的结果是(0,0),(2,1),(2,3)