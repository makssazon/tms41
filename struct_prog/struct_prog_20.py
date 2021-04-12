# В массиве целых чисел с количеством элементов 19
# определить максимальное число и заменить им все
# четные по значению элементы. [02-4.1-BL19]
from random import randint

arr = [randint(1, 20) for i in range(19)]
print(arr, len(arr))
max_num = max(arr)
print(max_num)

for j, i in enumerate(arr):
    if not i % 2:
        arr[j] = max_num

print(arr)
