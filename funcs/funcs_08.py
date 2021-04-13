# Написать функцию принимающая на вход неопределенным
# количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое
# либо среднегеометрическое. Написать программу в виде трех функций.

def avg_geom(arr):
    result = 1
    for arg in arr:
        result *= arg
    result **= 1 / len(arr)
    return result


def avg_arifm(arr):
    result = 0
    for arg in arr:
        result += arg
    result /= len(arr)
    return result


def func(*args, mean_type):
    if mean_type == 'geo':
        return avg_geom(args)
    if mean_type == 'arif':
        return avg_arifm(args)


def main():
    print(func(1, 2, 3, 4, 5, mean_type='arif'))
    print(func(1, 2, 3, 4, 5, mean_type='geo'))


if __name__ == '__main__':
    main()
