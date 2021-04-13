# Создать функцию, принимающая на вход неопределенное
# количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10


def func(*args):
    result = 0
    for i, arg in enumerate(args):
        result += i * arg
    return result


def main():
    print(func(4, 3, 2, 1))


if __name__ == '__main__':
    main()
