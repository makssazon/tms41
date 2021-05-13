# Создать бесконечный генератор случайных чисел.
# Генератор должен принимать диапазон случайных чисел и смещение
from random import randint
from time import sleep


def gen_random(start=1, stop=10, step=10):
    while True:
        yield randint(start, stop)
        sleep(0.5)
        start += step
        stop += step


def main():
    my_generator = gen_random()
    for i in my_generator:
        print(i)


if __name__ == '__main__':
    main()
