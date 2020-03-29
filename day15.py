# numpy中的nan和inf
import numpy as np

# 什么时候numpy中会出现nan：
# 当我们读取本地的文件为float的时候，如果有缺失，就会出现nan 当做了一个不合适的计算的时候(比如无穷大(inf)减去无穷大)
# nan和任何职计算都为nan

# inf(-inf,inf):infinity,inf表示正无穷，-inf表示负无穷
# 什么时候回出现inf包括（-inf，+inf） 比如一个数字除以0，（python中直接会报错，numpy中是一个inf或者-inf）

# a = np.inf
# print(type(a))  <class 'float'>
# b = np.inf
# print(type(b))  <class 'float'>

# 两个nan是不相等的
# np.nan == np.nan False
# np.nan != np.nan True

t1 = np.arange(24)
t1 = t1.reshape(4,6)
print(t1)
# # 统计数组中不等于0的个数
# print(np.count_nonzero(t1))
#
# # 返回bool类型的数组中是否含有nan
# print(np.isnan(t1))
# t2 = np.array(t1,dtype = float)
#
# t2[0,0] = np.nan
# print(t2)
# print(np.isnan(t2))
#
# # 统计numpy中nan的个数
# print(np.count_nonzero(t2!=t2))
# print(np.count_nonzero(np.isnan(t2)))

# 利用轴对数组求和
# print(np.sum(t1))
# print(np.sum(t1,axis=0))
# print(np.sum(t1,axis=1))

# numpy中常用统计函数
# 求和：t.sum(axis=None)
# 均值：t.mean(a,axis=None) 受离群点的影响较大
# 中值：np.median(t,axis=None)
# 最大值：t.max(axis=None)
# 最小值：t.min(axis=None)
# 极值：np.ptp(t,axis=None) 即最大值和最小值只差
# 标准差：t.std(axis=None)
# 默认返回多维数组的全部的统计结果,如果指定axis 则返回一个当前轴上的结果