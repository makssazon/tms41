# Написать функцию, которая получает на вход имя
# и выводит строку вида: “Hello, {name}”.
# Создать список из 5 имен.
# Вызвать функцию для каждого элемента списка в цикле.

def func(name):
    print(f'Hello, {name}')


arr = ['maks', 'igor', 'pyatro', 'abram', 'valera']

for name in arr:
    func(name)
