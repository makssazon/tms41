# Написать функцию по решению квадратных уравнений.
# [01-11.2-Proc17]

def func(a=0, b=0, c=0):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return 0, 0
    if D == 0:
        x_1 = (- b + D ** 0.5) / 2 * a
        return x_1, x_1
    else:
        x_1 = (- b + D ** 0.5) / 2 * a
        x_2 = (- b - D ** 0.5) / 2 * a
        return x_1, x_2


def main():
    print(func(1, 12, 36))


if __name__ == '__main__':
    main()
