# Создать файл dog.py.
# Создать пустой класс Dog

class Dog:
    def __init__(self, height, weight, name, age, master, adress='Minsk'):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__adress = adress

    def change_name(self, name):
        self.name = name

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Bark!')

    def get_master(self):
        return self.__master

    def get_adress(self):
        return self.__adress

    def set_adress(self, adress):
        self.__adress = adress


dog_1 = Dog(0.7, 15, 'Baskerviley', 31, 'nub')

print(dog_1)

dog_1.jump()
dog_1.run()
dog_1.bark()
print(dog_1.height, dog_1.weight, dog_1.name, dog_1.age)

dog_1.change_name('Sharik')
print(dog_1.name)
print(dog_1.get_master())
print(dog_1.get_adress())
dog_1.set_adress('Drybin')
print(dog_1.get_adress())
