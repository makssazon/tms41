# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.
from random import randint


def func_matrix(n, m):
    matrix = [[randint(1, 10) for element in range(m)] for row in range(n)]
    sum_matrix = 0
    max_elements = []
    min_elements = []
    for row in matrix:
        print(row)
        sum_matrix += sum(row)
        max_elements.append(max(row))
        min_elements.append((min(row)))
    print(f'summa : {sum_matrix}, max element : '
          f'{max(max_elements)}, min element : {min(min_elements)}')


func_matrix(4, 4)
