#numpy数值的修改

import numpy as np

t1 = np.arange(24)
t1 = t1.reshape(4,6)
print(t1)

# 修改第三行和第四列的数值为0
# print(t1[:,2:4])
# t1[:,2:4] = 0
# print(t1)

# # 修改小于10的值为3
# print(t1 < 10)
# t1[t1<10] = 3
# print(t1)

# numpy中三元运算符
# 将小于10的替换成100，大于等于10的替换成1000
# print(np.where(t1<10,100,1000))

# numpy中的clip(裁剪)
# print(t1.clip(10,18))

