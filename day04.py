from  matplotlib import pyplot


x1 = range(1,32)
x2 = range(51,82)
a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]


x = x1

pyplot.xticks(range(1,32))

pyplot.scatter(x1,a)

pyplot.scatter(x2,b)


pyplot.show()