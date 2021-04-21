# Создать функцию, которая принимает на вход
# неопределенное количество аргументов и
# возвращает их сумму и максимальное из них.


def func(*args):
    sum_args = sum(args)
    max_args = max(args)
    return sum_args, max_args


def main():
    print(func(1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()
