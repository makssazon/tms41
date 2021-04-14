# Дан массив целых чисел A.
# Найти суммы положительных и отрицательных
# элементов массива, используя функцию определения суммы.
# [02-5.1-BL21]
from random import randint
from typing import List, Tuple


def func(arr: List[int]) -> Tuple[int, int]:
    result_positiv = 0
    result_negativ = 0
    for i in arr:
        if i > 0:
            result_positiv += i
        else:
            result_negativ += i
    return result_negativ, result_positiv


def main():
    arr = [randint(-10, 10) for i in range(5)]
    print(arr)
    print(func(arr))


if __name__ == '__main__':
    main()
