# Дан произвольный список, содержащий только числа.
# Выведите результат сложения всех чисел больше 10.
from random import randint

list_num = [randint(-20, 20) for i in range(10)]
list_2 = list_num.copy()
print(list_num)

result = 0
len_list = len(list_num)
while len_list:
    num = list_num[len_list - 1]
    if num > 10:
        result += num
    len_list -= 1
print(result)

result = 0
while list_num:
    num = list_num.pop()
    if num > 10:
        result += num
print(result)

result_2 = sum(list(filter(lambda x: x > 10, list_2)))
print(result_2)
