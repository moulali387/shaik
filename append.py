import numpy
a = numpy.array([[3, 4,5], [6,7,8]])
b = numpy.array([[600], [700]])
c = numpy.array([[1, 2, 3], [4, 5, 6]])
x = numpy.append(a, b, axis=1) #adding a column 
print("new array after adding column")
print(x)
y = numpy.append(c, [[50, 60, 70]], axis = 0) #adding a row
print("new array after adding row")
print(y)
