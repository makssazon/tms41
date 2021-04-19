# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку
# данных - удалять все четные элементы из списка.
from functools import wraps
from random import randint


def my_decorator(func):
    @wraps(func)
    def wrapper(arr):
        arr = list(filter(lambda x: not x % 2, arr))
        func(arr)

    return wrapper


@my_decorator
def my_func(arr):
    print(f'important action with {arr}')


def main():
    arr = [randint(-10, 10) for i in range(10)]
    print(arr)
    my_func(arr)


if __name__ == '__main__':
    main()
