from  matplotlib import pyplot
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname = '/System/Library/Fonts/PingFang.ttc')

x1 = range(1,32)
x2 = range(71,102)
a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

#设置图形大小
pyplot.figure(figsize= (20,9),dpi = 80)

#调整x轴的刻度
_x = list(x1) + list(x2)
_xticks = ['3月{}号'.format(i) for i in x1]
_xticks += ['10月{}号'.format(i - 70) for i in x2]
pyplot.xticks(_x[::3],_xticks[::3],fontproperties = my_font,rotation = 45)

#使用scatter方法绘制散点图
pyplot.scatter(x1,a,label = '3月份')
pyplot.scatter(x2,b,label = '10月份')

#添加图例
pyplot.legend(loc = 'upper left',prop = my_font)

#添加描述信息
pyplot.xlabel("时间",fontproperties = my_font)
pyplot.ylabel("温度",fontproperties = my_font)
pyplot.title("标题",fontproperties = my_font)

#展示
pyplot.show()