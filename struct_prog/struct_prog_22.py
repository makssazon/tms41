# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]
from random import randint

matrix = [[randint(1, 10) for element in range(4)] for row in range(4)]
for row in matrix:
    print(row)

for i, row in enumerate(matrix):
    max_digit = max(row)
    index_max = row.index(max_digit)
    if i != index_max:
        row[i], row[index_max] = row[index_max], row[i]

print('result: ')
for row in matrix:
    print(row)
