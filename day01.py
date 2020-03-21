from matplotlib import  pyplot

#设置图片大小
pyplot.figure(figsize=(18,9),dpi = 60)

x = range(2,26,2)

y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

#设置x刻度
pyplot.xticks(range(2,26))

#设置y刻度
pyplot.yticks(range(min(y),(max(y)+1)))

pyplot.plot(x,y)

#保存图片
#pyplot.savefig("data01.png")

pyplot.show()