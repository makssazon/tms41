# Дан список чисел. Вернуть список, где каждый
# число переведено в строку
# [5, 3] -> [‘5’, ‘3’]
from random import randint

arr = [randint(1, 20) for i in range(10)]
print(arr)
new_arr = list(map(lambda x: str(x), arr))
print(new_arr)
