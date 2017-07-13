class Matrix(object):
  def __init__(self, matrix):
    if (type(matrix[0]) is list):
      self.matrix = matrix
      self.rows = len(matrix)
      self.cols = len(matrix[0])
    else:
      self.matrix = [matrix]
      self.rows = len(self.matrix)
      self.cols = len(self.matrix[0])

  def is_vector(self):
    return self.rows == 1 or self.cols == 1

  def print_matrix(self):
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
