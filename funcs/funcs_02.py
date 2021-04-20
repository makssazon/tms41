# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.
from random import randint


def create_matrix(n, m):
    matrix = [[randint(1, 10) for element in range(m)] for row in range(n)]
    return matrix


def read_matrix(matrix):
    for row in matrix:
        print(row)


def sum_matrix(matrix):
    sum_matrix = 0
    for row in matrix:
        sum_matrix += sum(row)
    return sum_matrix


def min_element(matrix):
    min_element = min([min(row) for row in matrix])
    return min_element


def max_element(matrix):
    max_element = max([max(row) for row in matrix])
    return max_element


def main():
    matrix = create_matrix(4, 4)
    read_matrix(matrix)
    print(sum_matrix(matrix))
    print(min_element(matrix))
    print(max_element(matrix))


if __name__ == '__main__':
    main()
