# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями от 1 до 9.
from random import randint

n = int(input("enter n - "))

for i in range(n):
    for j in range(n):
        print(randint(1, 9), end=' ')
    print()
