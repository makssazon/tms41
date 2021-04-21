# Создать файл animals.py. Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы:
# run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.


class Pet:

    def run(self):
        print('Run!')

    def jump(self):
        print('jump!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep!')


class Dog(Pet):
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def bark(self):
        print('Bark!')


class Cat(Pet):
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def meow(self):
        print('Meow!')


class Parrot(Pet):
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def fly(self):
        print('Fly!')


dog = Dog('rex', 10, 'igar')
dog.jump()
dog.birthday()
print(dog.age)
dog.sleep()
dog.bark()
dog.run()

cat = Cat('murka', 5, 'Valera')
cat.run()
cat.sleep()
cat.jump()
cat.birthday()
print(cat.age)
cat.meow()

parrot = Parrot('gosha', 3, 'Alla')
parrot.run()
parrot.jump()
parrot.sleep()
parrot.birthday()
parrot.fly()
