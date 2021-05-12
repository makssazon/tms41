# Создать файл test_matrix в пакете test.
# Протестировать конструктор,магический метод __str__ класса Matrix.
# В отдельном классе теста протестировать функции по работе с матрицами
from unittest import TestCase
from unittest.mock import MagicMock, patch

from oop.matrix import Matrix, max_element, min_element, sum_matrix


class TestMatrix(TestCase):
    def setUp(self):
        self.result = [[0 for element in range(5)] for row in range(5)]
        self.matrix = Matrix()
        self.matrix2 = Matrix(self.matrix)

    def test_init(self):
        self.assertEqual(self.matrix._Matrix__n, 5)
        self.assertEqual(self.matrix._Matrix__m, 5)
        self.assertEqual(self.matrix._Matrix__data, self.result)
        self.assertListEqual(self.matrix._Matrix__data, self.result)

    def test_init_with_data(self):
        self.assertEqual(self.matrix2._Matrix__n, 5)
        self.assertEqual(self.matrix2._Matrix__m, 5)
        self.assertEqual(self.matrix2._Matrix__data, self.result)
        self.assertListEqual(self.matrix2._Matrix__data, self.result)

    def test_str(self):
        self.assertEqual(self.matrix.__str__(), str(self.result))


class TestMatrixDef(TestCase):
    @patch('oop.matrix.max')
    @patch('oop.matrix.Matrix')
    def test_max_element(self, mock_matrix, mock_max):
        matrix = mock_matrix()
        matrix.data = [[1, 2, 3], [2, 1, 4]]
        mock_max.side_effect = [3, 4, 4]
        self.assertEqual(max_element(matrix), 4)

    @patch('oop.matrix.min')
    def test_min_element(self, mock_min):
        matrix = MagicMock(data=[[0, 2, 3], [2, 1, 4]])
        mock_min.side_effect = [0, 1, 0]
        self.assertEqual(min_element(matrix), 0)

    @patch('oop.matrix.sum')
    def test_sum_elements(self, mock_sum):
        matrix = MagicMock(data=[[0, 2, 3], [2, 1, 4]])
        mock_sum.side_effect = [5, 7, 12]
        self.assertEqual(sum_matrix(matrix), 12)
