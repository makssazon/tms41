# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint

n = int(input("enter n - "))
result = 0
for i in range(n):
    for j in range(n):
        num = randint(1, 10)
        print(num, end=' ')
        if not num % 3:
            result += num
    print()
print("Найти сумму всех элементов матрицы, которые кратны 3 - ", result)
