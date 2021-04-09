# Дан список целых чисел. Подсчитать
# сколько четных чисел в списке

from random import randint

arr = [randint(1, 10) for _ in range(7)]
print(arr)

result = list(filter(lambda x: not x % 2, arr))
print(result)
print(len(result))
