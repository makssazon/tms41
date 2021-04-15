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
for row in massiv:
    for element in row:
        result += element
        len_mas += 1
avg = result / len_mas
print(f"summa = {result}, len - {len_mas}, avg = {avg}")

result_2 = 0

for i, row in enumerate(massiv):
    for j, element in enumerate(row):
        if not (i + j) % 2 and element > avg:
            result_2 += 1
print('itog = ', result_2)
