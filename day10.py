#nump学习


import numpy as np
import random

#使用numpy生成数组，得到ndarray的数据类型
t1 = np.array([1,2,3])
print(t1)
print(type(t1))


t2 = np.array(range(1,10))
print(t2)
print(type(t2))

#numpy中自有的方法，效果如同np.array(range1,10))
t3 = np.arange(10)
print(t3)
print(type(t3))

print(t3.dtype)

#numpy中的数据类型
t4 = np.array(range(1,4),dtype = float)
print(t4.dtype)

t4 = np.array(range(1,4),dtype = "float32")
print(t4.dtype)

t5 = np.array([2,1,1,1,6],dtype = bool)
print(t5)
print(t5.dtype)

#调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

#numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)

#numpy中保留两位小数
t8 = np.round(t7,2)
print(t8)

#python中保留两位小数
t9= round(random.random(),3)
print(t9)

