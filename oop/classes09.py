# Создать файл classes09.py. Создать
# пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.

class Man:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def sing(self):
        print('la la la!')

    def drink(self):
        print('Beer!')


man = Man('Igar', 31, 180)
print(man._Man__name)
print(man.name)


class Car:
    def __init__(self, brand, age, engine):
        self.__brand = brand
        self.__age = age
        self.__engine = engine

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    def start(self):
        print('Start!')

    def finish(self):
        print('Finish!')


car = Car('ford', 25, '2.5 dizel')
print(car.brand, car.engine, car.age)


class PC:
    def __init__(self, brand, system, engine):
        self.__brand = brand
        self.__system = system
        self.__engine = engine

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    def start(self):
        print('Start!')

    def finish(self):
        print('Finish!')


class Motorcycle:
    def __init__(self, brand, year, engine):
        self.__brand = brand
        self.__year = year
        self.__engine = engine

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    def start(self):
        print('Start!')

    def finish(self):
        print('Finish!')


class Drink:
    def __init__(self, type, strength, color):
        self.__type = type
        self.__strength = strength
        self.__color = color

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        self.__strength = strength

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def buy(self):
        print(f'Buy {self.__type}!')

    def drink(self):
        print(f'Finish drink {self.__type}!')


drink = Drink('wisky', 43, 'gold')
print(drink.type, drink.color, drink.strength)
drink.buy()
drink.drink()
drink.strength = 40
print(drink.strength)
