# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint

n = int(input("enter n - "))

massiv = [[randint(1, 10) for j in range(n)] for i in range(n)]
print(massiv)
result = 0
for row in massiv:
    for element in row:
        if not element % 3:
            result += element
print("Найти сумму всех элементов матрицы, которые кратны 3 - ", result)
