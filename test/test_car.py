# Создать файл test_car в пакете test. Протестировать
# конструктор, метод увеличения скорости, уменьшения
# скорости, остановки, разворота класса Car в файле oop/car10
from unittest import TestCase

from oop.car10 import Car


class CarTestCase(TestCase):
    def test_init(self):
        car = Car('lada', 'priora', 2010, 90)
        self.assertEqual(car._Car__brand, 'lada')
        self.assertEqual(car._Car__model, 'priora')
        self.assertEqual(car._Car__year, 2010)
        self.assertEqual(car._Car__speed, 90)

    def test_init_speed_none(self):
        car = Car('lada', 'priora', 2010)
        self.assertEqual(car._Car__brand, 'lada')
        self.assertEqual(car._Car__model, 'priora')
        self.assertEqual(car._Car__year, 2010)
        self.assertEqual(car._Car__speed, 0)

    def test_speed_plus(self):
        car = Car('lada', 'priora', 2010)
        car.speed_plus()
        self.assertEqual(car._Car__speed, 5)

    def test_speed_minus(self):
        car = Car('lada', 'priora', 2010, 90)
        car.speed_minus()
        self.assertEqual(car._Car__speed, 85)

    def test_stop(self):
        car = Car('lada', 'priora', 2010, 90)
        car.stop()
        self.assertEqual(car._Car__speed, 0)

    def test_reverse(self):
        car = Car('lada', 'priora', 2010, 90)
        car.reverse()
        self.assertEqual(car._Car__speed, -90)
