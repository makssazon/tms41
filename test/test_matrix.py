# Создать файл test_matrix в пакете test.
# Протестировать конструктор,магический метод __str__ класса Matrix.
# В отдельном классе теста протестировать функции по работе с матрицами
from unittest import TestCase

from oop.matrix import Matrix


class TestMatrix(TestCase):
    def test_init(self):
        result = [[0 for element in range(5)] for row in range(5)]
        matrix = Matrix()
        self.assertEqual(matrix._Matrix__n, 5)
        self.assertEqual(matrix._Matrix__m, 5)
        self.assertEqual(matrix._Matrix__data, result)
        self.assertListEqual(matrix._Matrix__data, result)

    def test_str(self):
        result = [[0 for element in range(5)] for row in range(5)]
        matrix = Matrix()
        self.assertEqual(matrix.__str__(), str(result))
