# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
#  >> first_number = int(first_number)


num_1 = int(input(" enter int number "))
num_2 = int(input(" enter second int number "))
print(f" {num_1} + {num_2} = {num_1 + num_2}")
result = num_1 + num_2
print("{} + {} = {}".format(num_1, num_2, result))
