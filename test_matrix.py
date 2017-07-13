import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):

  def test_init(self):

    test_matrix = Matrix([[1,2,3],[4,5,6]])
    self.assertEqual(test_matrix.rows, 2)
    self.assertEqual(test_matrix.cols, 3)
    self.assertEqual(test_matrix.matrix, [[1,2,3],[4,5,6]])

    test_matrix = Matrix([1,2,3,4])
    self.assertEqual(test_matrix.rows, 1)
    self.assertEqual(test_matrix.cols, 4)
    self.assertEqual(test_matrix.matrix, [[1,2,3,4]])

  def test_identity(self):
    test_matrix = Matrix.identity(1)
    single_identity = [[1]]
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

  def test_is_vector(self):
    test_matrix = Matrix([1,2,3,4])
    self.assertTrue(test_matrix.is_vector())

    test_matrix = Matrix([[1],[2],[3]])
    self.assertTrue(test_matrix.is_vector())

    test_matrix = Matrix([[1,2], [3,4]])
    self.assertFalse(test_matrix.is_vector())

  def test_transpose(self):
    original = Matrix([[1,3,5], [2,4,6]])
    transpose = [[1,2],[3,4],[5,6]]
    self.assertEqual(original.transpose().matrix, transpose)

    original = Matrix([1,2,3,4])
    transpose = [[1],[2],[3],[4]]
    self.assertEqual(original.transpose().matrix, transpose)

    original = Matrix([[1],[2],[3],[4]])
    transpose = [[1,2,3,4]]
    self.assertEqual(original.transpose().matrix, transpose)

  def test_zeros(self):
    original = Matrix.zeros(2,3)
    self.assertEqual(original.matrix, [[0,0,0],[0,0,0]])

    original = Matrix.zeros(1,5)
    self.assertEqual(original.matrix, [[0,0,0,0,0]])

    original = Matrix.zeros(5,1)
    self.assertEqual(original.matrix, [[0],[0],[0],[0],[0]])

  def test_scale(self):
    original = Matrix([1,2,3,4])
    self.assertEqual(original.scale(2).matrix, [[2,4,6,8]])

    original = Matrix([[1,2,3], [4,5,6]])
    self.assertEqual(original.scale(.5).matrix, [[.5,1,1.5], [2,2.5,3]])

def main():
  unittest.main()

if __name__ == '__main__':
  main()
