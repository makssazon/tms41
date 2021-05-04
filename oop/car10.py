# Создать файл car10.py. Создать класс Car.
# Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5),
# стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_plus(self):
        self.__speed += 5

    def speed_minus(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def print_speed(self):
        print(f'speed = {self.__speed}')

    def reverse(self):
        self.__speed = - self.__speed


car = Car('lada', 'priora', 2011, 120)
car.speed_plus()
car.print_speed()
