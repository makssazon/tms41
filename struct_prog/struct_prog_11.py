# Дан список целых чисел.
# Создать новый список, каждый элемент
# которого равен исходному элементу умноженному на -2
from random import randint

arr = [randint(1, 10) for _ in range(7)]
print(arr)
new_arr = list(map(lambda x: x * (- 2), arr))
print(new_arr)

new_arr_2 = []
for i in arr:
    new_arr_2.append(i * (- 2))
print(new_arr_2)
