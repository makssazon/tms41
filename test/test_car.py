# Создать файл test_car в пакете test. Протестировать
# конструктор, метод увеличения скорости, уменьшения
# скорости, остановки, разворота класса Car в файле oop/car10
from unittest import TestCase

from oop.car10 import Car


class CarTestCase(TestCase):
    def setUp(self):
        self.car1 = Car('lada', 'priora', 2010, 90)
        self.car2 = Car('lada', 'priora', 2010)

    def test_init(self):
        self.assertEqual(self.car1._Car__brand, 'lada')
        self.assertEqual(self.car1._Car__model, 'priora')
        self.assertEqual(self.car1._Car__year, 2010)
        self.assertEqual(self.car1._Car__speed, 90)

    def test_init_speed_none(self):
        self.assertEqual(self.car2._Car__brand, 'lada')
        self.assertEqual(self.car2._Car__model, 'priora')
        self.assertEqual(self.car2._Car__year, 2010)
        self.assertEqual(self.car2._Car__speed, 0)

    def test_speed_plus(self):
        self.car2.speed_plus()
        self.assertEqual(self.car2._Car__speed, 5)

    def test_speed_minus(self):
        self.car1.speed_minus()
        self.assertEqual(self.car1._Car__speed, 85)

    def test_stop(self):
        self.car1.stop()
        self.assertEqual(self.car1._Car__speed, 0)

    def test_reverse(self):
        self.car1.reverse()
        self.assertEqual(self.car1._Car__speed, -90)
