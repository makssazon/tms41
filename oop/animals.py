# Создать файл animals.py. Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы:
# run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.


class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def __eq__(self, other):
        return (type(self), self.age, self.height, self.weight) \
               == (type(other), other.age, other.height, other.weight)

    def __ne__(self, other):
        return not (type(self), self.age, self.height, self.weight) \
                   == (type(other), other.age, other.height, other.weight)

    def run(self):
        print('Run!')

    def jump(self, height):
        print(f'jump {height} meters')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep!')

    def voice(self):
        pass

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.2

    def change_height(self, arg=None):
        if arg:
            self.height += arg
        else:
            self.height += 0.2


class Dog(Pet):

    def voice(self):
        print('Bark!')

    def jump(self, height):
        if height > 0.5:
            print('Dogs can not jump so hight')
        else:
            super().jump(height)


class Cat(Pet):

    def voice(self):
        print('Meow!')

    def jump(self, height):
        if height > 2:
            print('Dogs can not jump so hight')
        else:
            super().jump(height)


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.05

    def fly(self):
        if self.weight > 0.1:
            print('This parrot can not fly')
        else:
            print('Fly!')

    def jump(self, height):
        if height > 0.05:
            print('Parrots can not jump so hight')
        else:
            super().jump(height)

    def voice(self):
        print('Fiu!')


class Horse(Pet):
    def voice(self):
        print('Igo-go')


class Donkey(Pet):
    def voice(self):
        print('Ia-ia-ia')


class Mule(Donkey, Horse):
    pass


parrot = Parrot('rex', 10, 'igar', 0.03, 0.5, 'voron')
parrot.jump(1)
parrot.birthday()
print(parrot.age)
parrot.sleep()
parrot.fly()
parrot.run()
parrot.change_height(1)
parrot.change_weight()
print(parrot.height, parrot.weight, parrot.species)
print()


def voice_animals(arr):
    for animal in arr:
        animal.voice()


def main():
    arr = [Dog('rex', 10, 'igar', 2, 0.5),
           Cat('rex', 10, 'igar', 1, 0.2),
           Parrot('rex', 10, 'igar', 0.03, 0.5, 'voron'),
           Mule('rex', 10, 'igar', 0.03, 0.5)]
    voice_animals(arr)


if __name__ == '__main__':
    main()

print(Dog('rex', 10, 'igar', 2, 1) == Dog('rex', 10, 'igar', 2, 1))
print(Dog('rex', 10, 'igar', 2, 1) != Dog('rex', 10, 'igar', 2, 1))
