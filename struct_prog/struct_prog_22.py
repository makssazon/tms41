# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]
from random import randint

matrix = [[randint(1, 10) for j in range(4)] for i in range(4)]
for i in matrix:
    print(i)

for j, i in enumerate(matrix):
    max_digit = max(i)
    index_max = i.index(max_digit)
    if j != index_max:
        i[j], i[index_max] = i[index_max], i[j]

print('result')
for i in matrix:
    print(i)
