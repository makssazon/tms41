# Ввести строку. Если длина строки больше 10 символов,
# то создать новую строку с 3 восклицательными знаками
# в конце  ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки

my_str = input('enter string : ')
if len(my_str) > 10:
    my_str_new = my_str + "!!!"
    print(my_str_new)
elif len(my_str) > 1:
    print(my_str[1])
else:
    print('too small')
