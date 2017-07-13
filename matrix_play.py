from matrix import Matrix

b = Matrix([[1,3,5], [2,4,6]])
b.print_matrix()

c = Matrix([[1,2,3], [4,5,6]])

d = Matrix([[2,2], [2,2], [2,2]])
d.print_matrix()

e = b.transpose()
e.print_matrix()

f = Matrix.identity(4)
f.print_matrix()

g = Matrix([[1],[2]])
g.print_matrix()
g.transpose().print_matrix()
