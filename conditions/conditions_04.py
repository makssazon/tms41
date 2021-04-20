# Ввести строку с клавиатуры
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку “Need more!”
# Если длина строки равна 5 - вывести строку “It is five”

my_str = input("enter str - ")

len_str = len(my_str)
if len_str > 5:
    print(my_str)
elif len_str < 5:
    print("need more")
else:
    print('it is 5')
