from Matrix import Matrix

b = Matrix([[1,3,5], [2,4,6]])
b.printMatrix()

c = Matrix([[1,2,3], [4,5,6]])

d = Matrix([[2,2], [2,2], [2,2]])
d.printMatrix()

e = b.transpose()
e.printMatrix()

f = Matrix.identity(4)
f.printMatrix()
