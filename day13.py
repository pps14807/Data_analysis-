#numpy读取数据和转置

import numpy as np

t1 = np.loadtxt("./youtube_video_data/US_video_data_numbers.csv",delimiter = ',',dtype = 'int')
print(t1)
print("--"*100)


#转置
t1 = np.loadtxt("./youtube_video_data/US_video_data_numbers.csv",delimiter = ',',dtype = 'int',unpack=True)
print(t1)

t2 = np.array([[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17]])
print(t2)
print(t2.transpose())
print(t2.swapaxes(1,0))
print(t2.T)