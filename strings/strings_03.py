# Создать произвольную строку. Получить подстроку с третьего
# элемента и до конца. Написать два решения с использованием
# полной и сокращенной записи

my_string = "1234567890"
abgrade_my_string = my_string[2:len(my_string):1]
super_abgrade_my_string = my_string[2:]
print(abgrade_my_string, super_abgrade_my_string)
