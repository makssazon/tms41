# Создать список произвольного содержания. После каждой операции
# выводить список на экран
# Добавить к нему строку “Hello”.
# Удалить первый элемент.
# Поменять второй элемент на строку “World”.
# Удалить элемент “World”
# Вывести на экран перевернутый список


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.append("hello")
print(my_list)

my_list.pop(0)
print(my_list)

my_list[1] = "World"
print(my_list)

my_list.remove("World")
print(my_list)

print(my_list[::-1])
