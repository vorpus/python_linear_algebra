class Matrix(object):
  def __init__(self, matrix):
    self.matrix = matrix
    self.rows = len(matrix)
    if (type(matrix[0]) is list):
      self.cols = len(matrix[0])
    else:
      self.cols = 1

  def printMatrix(self):
    print "Matrix: {0}x{1}".format(self.rows, self.cols)
    for i in range(0, self.rows):
      print " ",
      if (self.cols > 1):
        for j in range(0,self.cols):
          print str(self.matrix[i][j]) + " ",
      else:
        print str(self.matrix[i]) + " ",
      print ""

  def transpose(self):
    new_matrix = []
    for i in range(0, self.cols):
      new_matrix.append([])
      for j in range(0, self.rows):
        new_matrix[i].append(self.matrix[j][i])
    return Matrix(new_matrix)

  # def scale(self, scalar):
  #   new_matrix = []
  #   for i in range(0, self.rows):

  @staticmethod
  def identity(size):
    id_matrix = []
    for i in range(0, size):
      if (size > 1):
        id_matrix.append([])
        for j in range(0, size):
          if (i == j):
            id_matrix[i].append(1)
          else:
            id_matrix[i].append(0)
      else:
        id_matrix.append(1)
    return Matrix(id_matrix)
