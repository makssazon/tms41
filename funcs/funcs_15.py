# Описать функцию fact2( n ), вычисляющую двойной факториал
# :n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 — параметр целого типа.
#     С помощью этой функции найти двойные
# факториалы пяти данных целых чисел [01-11.2-Proc35]


def fact2(num):
    result = 1
    if num % 2:
        for i in range(1, num + 1, 2):
            result *= i
    else:
        for i in range(2, num + 1, 2):
            result *= i
    return result


def main():
    arr = [2, 3, 4, 5, 6]
    for i in arr:
        print(fact2(i))


if __name__ == '__main__':
    main()
