import numpy as np

#shape标识numpy的形状，表示几行几列的数组；shape几个数就是几维数组

#一位数组
t1 = np.arange(12)
print(t1)
print(t1.shape)  #元组

#二维数组
t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

#三维数组
t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
print(t3.shape)

#reshape改变元组的形状
t4 = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
print(t4)
t5 = t4.reshape(3,4)   #3*4 =12
print(t5)

t6 = np.arange(24)
t7 = t6.reshape(2,3,4)  # 2*3*4 = 24
print(t7)

print(t7.reshape(4,6))  # 变成二维数组数组
print(t7.reshape(24,))  # 变成一位数组
print(t7.reshape(24,1))  # 变成二维数组
print(t7.reshape(1,24))  # 变成二维数组

print('*' * 10)
#将一个不知道的数组变成一维数组
t8 = t5.reshape((t5.shape[0] * t5.shape[1],))   # t5.shape[0] * t5.shape[1]  = 行数*列数
print(t8)
t8 = t5.flatten()  #flatten扁平化处理
print(t8)