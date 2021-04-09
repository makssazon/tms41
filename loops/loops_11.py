# Дан двумерный массив n × m элементов.
# Определить, сколько раз встречается число
# 7 среди элементов массива.[02-4.2-BL12]
from random import randint

n = int(input('enter n - '))
m = int(input('enter m - '))

massiv = [[randint(1, 10) for j in range(m)] for i in range(n)]
print(massiv)

result = 0
for i in massiv:
    for j in i:
        if j == 7:
            result += 1
print(f"result = {result}")
