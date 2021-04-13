# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется как
# произведение всех натуральных чисел от 1 до n включительно


def func(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)
    return result


def main():
    func(3)


if __name__ == '__main__':
    main()
