# Создать файл dog.py.
# Создать пустой класс Dog

class Dog:
    def __init__(self, height, weight, name, age, master, adress='Minsk'):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__adress = adress

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

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
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress):
        self.__adress = adress

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Bark!')


dog_1 = Dog(0.7, 15, 'Baskerviley', 31, 'nub')

print(dog_1)

dog_1.jump()
dog_1.run()
dog_1.bark()

print(dog_1.height, dog_1.adress, dog_1.master)
dog_1.height = 1
print(dog_1.height)
