import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):

  def test_identity(self):
    test_matrix = Matrix.identity(1)
    single_identity = [1]
    self.assertEqual(test_matrix.matrix, single_identity)

    test_matrix = Matrix.identity(2)
    two_identity = [[1,0], [0,1]]
    self.assertEqual(test_matrix.matrix, two_identity)

    test_matrix = Matrix.identity(4)
    four_identity = [
      [1,0,0,0],
      [0,1,0,0],
      [0,0,1,0],
      [0,0,0,1]
    ]
    self.assertEqual(test_matrix.matrix, four_identity)

  def test_transpose(self):
    original = Matrix([[1,3,5], [2,4,6]])
    transpose = [[1,2],[3,4],[5,6]]
    self.assertEqual(original.transpose().matrix, transpose)

    original = Matrix([1,2,3,4])
    transpose = [[1],[2],[3],[4]]
    self.assertEqual(original.transpose().matrix, transpose)


def main():
  unittest.main()

if __name__ == '__main__':
  main()
