# Рассчитать значение х определив и
# использовав необходимую функции. [02-5.1-BL01]


def element(arg):
    return (arg ** (1 / 2) + arg) / 2


def func(*args):
    result = 0
    for arg in args:
        result += element(arg)
    return result


def test_alement():
    result = element(1)
    assert result == 1


def test_func_sum():
    result = func(1, 1, 1)
    assert result == 3
