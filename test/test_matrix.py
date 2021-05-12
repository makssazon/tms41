# Создать файл test_matrix в пакете test.
# Протестировать конструктор,магический метод __str__ класса Matrix.
# В отдельном классе теста протестировать функции по работе с матрицами
from unittest import TestCase

from oop.matrix import Matrix


class TestMatrix(TestCase):
    def setUp(self):
        self.result = [[0 for element in range(5)] for row in range(5)]
        self.matrix = Matrix()

    def test_init(self):
        self.assertEqual(self.matrix._Matrix__n, 5)
        self.assertEqual(self.matrix._Matrix__m, 5)
        self.assertEqual(self.matrix._Matrix__data, self.result)
        self.assertListEqual(self.matrix._Matrix__data, self.result)

    def test_str(self):
        self.assertEqual(self.matrix.__str__(), str(self.result))


class TestMatrixDef(TestCase):
    def test_max_element(self):
        pass
