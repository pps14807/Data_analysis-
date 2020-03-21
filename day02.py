from matplotlib import  pyplot
import random
import matplotlib
from matplotlib import  font_manager

my_font = font_manager.FontProperties(fname = "/System/Library/Fonts/PingFang.ttc")


x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

pyplot.figure(figsize=(18,9),dpi=80)

#调整x轴的刻度
_x = list(x)
_xtick_labels =["10点{}分".format(i) for i in  range(0,60)]
_xtick_labels += ["11点{}分".format(i) for i in range(0,60)]

pyplot.xticks(_x[::10],_xtick_labels[::10],rotation = 90,fontproperties=my_font)  #刻度显示字符串时，必须要数字和字符串一一对应

pyplot.xlabel("时间",fontproperties = my_font)
pyplot.ylabel("温度",fontproperties = my_font)
pyplot.title("10点到12点每分钟的时间变化情况",fontproperties = my_font)

pyplot.plot(x,y)

pyplot.show()


