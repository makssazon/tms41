# Дана целочисленная матрица А[n,m]. Посчитать количество
# элементов матрицы, превосходящих среднее арифметическое
# значение элементов матрицы и сумма индексов которых четна.[02-4.2-BL23]

from random import randint

n = int(input('enter n - '))
m = int(input('enter m - '))

massiv = [[randint(1, 10) for j in range(m)] for i in range(n)]
print(massiv)

len_mas = 0
result = 0
for i in massiv:
    for j in i:
        result += j
        len_mas += 1
avg = result / len_mas
print(f"summa = {result}, len - {len_mas}, avg = {avg}")

result_2 = 0

for i, j in enumerate(massiv):
    for i_1, j_1 in enumerate(j):
        if not (i + i_1) % 2 and j_1 > avg:
            result_2 += 1
print('itog = ', result_2)
