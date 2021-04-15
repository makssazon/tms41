# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями от 1 до 9.
from random import randint

n = int(input("enter n - "))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(randint(1, 9))
print(matrix)
