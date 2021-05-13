# Создать бесконечный генератор случайных чисел.
# Использовать в генераторе временную задержку
from random import randint
from time import sleep


def gen_random():
    while True:
        yield randint(-100, 100)
        sleep(0.5)


def main():
    my_generator = gen_random()
    for i in my_generator:
        print(i)


if __name__ == '__main__':
    main()
