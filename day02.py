from matplotlib import  pyplot
import random

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

pyplot.figure(figsize=(18,9),dpi=80)

#调整x轴的刻度
_x = x
_xtick_labels =["hello,{}".format(i) for i in _x]

pyplot.xticks(x,_xtick_labels)  #刻度显示字符串时，必须要数字和字符串一一对应

pyplot.plot(x,y)

pyplot.show()


