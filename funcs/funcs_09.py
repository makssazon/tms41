# Дан список чисел. Посчитать сколько раз встречается
# каждое число. Использовать функцию.
# Подсказка: для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре
# использовать метод get(), либо оператор in
from random import randint


def func(arr):
    dict = {}
    for i in arr:
        if not dict.get(i):
            dict[i] = 1
        else:
            dict[i] += 1

    return dict


def main():
    arr = [randint(1, 10) for i in range(20)]
    print(arr)
    print(func(arr))


if __name__ == '__main__':
    main()
