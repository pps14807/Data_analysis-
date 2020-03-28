#广播机制
import  numpy as np

t1 = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(t1)



print(t1 + 2)

print('--' * 20)

print(t1 / 2)

print('--' * 20)

t2 = np.array([0,1,2,3])
print(t1 + t2)

print('--' * 20)

t3 = np.array([[0],[1],[2]])
print(t1 + t3)