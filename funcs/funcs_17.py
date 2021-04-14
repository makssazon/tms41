# Описать функцию Sin1( x , ε ) вещественного типа
# (параметры x , ε — вещественные, ε > 0),
# находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ...
# + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые,
# модуль которых больше ε .
# С помощью Sin1 найти приближенное значение синуса
# для данного x при шести данных ε
# .  [01-11.3-Proc41]
import math


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def func(x, e):
    y = x
    result = 0
    n = 0
    while abs(y) > e:
        n_f = fact(2 * n + 1)
        y = ((-1) ** n * x ** (2 * n + 1)) / n_f
        result += y
        n += 1
    else:
        return result


def main():
    x = 1
    arr = [0, 0.01, 0.1, 0.2, 0.5, 1, 2]
    for e in arr:
        print(f'sin({x}) = {func(x, e)}, original sin({x}) = {math.sin(x)}')


if __name__ == '__main__':
    main()
