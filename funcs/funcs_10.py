# Рассчитать значение х определив и
# использовав необходимую функции. [02-5.1-BL01]


def element(arg):
    return (arg ** (1 / 2) + arg) / 2


def func(*args):
    result = 0
    for arg in args:
        result += element(arg)
    return result


def main():
    print(func(5, 12, 19))


if __name__ == '__main__':
    main()
