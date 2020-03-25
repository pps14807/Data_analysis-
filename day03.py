from matplotlib import pyplot
import matplotlib
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(10,30)
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

pyplot.xticks(x)
pyplot.yticks(range(min(y1),max(y1)+1))

pyplot.xlabel("年龄",fontproperties = my_font)
pyplot.ylabel("朋友数",fontproperties = my_font)
pyplot.title("每年交朋友的数量走势",fontproperties = my_font)


pyplot.plot(x,y1,color = 'r',linestyle = '-',linewidth = 1,label = '自己')
pyplot.plot(x,y2,color = 'g',linestyle = '--',linewidth = 2,label = '同桌')
pyplot.legend(prop = my_font,loc = 'best')
pyplot.grid(alpha = 0.6,linestyle = ':')
pyplot.show()