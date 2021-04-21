# Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).
from random import randint


def func(n, random_from=1, random_to=9):
    matrix = [[randint(random_from, random_to) for element in range(n)]
              for row in range(n)]
    return matrix


def main():
    print(func(5, -100, 500))


if __name__ == '__main__':
    main()
