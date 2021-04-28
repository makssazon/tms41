# Дан список чисел. Найти произведение всех чисел, которые кратны 3.
from functools import reduce
from random import randint

arr = [randint(1, 20) for i in range(10)]
print(arr)
new_arr = reduce(lambda x, y: x * y, filter(lambda x: not x % 3, arr))
print(new_arr)
