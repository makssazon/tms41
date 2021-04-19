# Создать универсальный декоратор, который
# меняет порядок аргументов в функции на противоположный.
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = tuple([arg for arg in args[::-1]])
        new_kwargs = {key: value for key, value in list(kwargs.items())[::-1]}
        func(new_args, new_kwargs)

    return wrapper


@my_decorator
def my_func(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)


def main():
    my_func(1, 2, 3, a=4, b=5, c=6)


if __name__ == '__main__':
    main()
