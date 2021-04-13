# Рассчитать значение х определив и
# использовав необходимую функции. [02-5.1-BL01]

def func(*args):
    result = 0
    for arg in args:
        result += (arg ** (1 / 2) + arg) / 2
    return result


def main():
    print(func(5, 12, 19))


if __name__ == '__main__':
    main()
