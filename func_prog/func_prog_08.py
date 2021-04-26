# Написать декоратор, который будет выводить время выполнения функции
# from datetime import datetime
# time = datetime.now()
from datetime import datetime
from functools import wraps
from time import sleep


def my_decorator(func):
    @wraps(func)
    def wrapper(t):
        start_time = datetime.now()
        result = func(t)
        delta_time = datetime.now() - start_time
        print(f'func run for next time : {delta_time}')
        return result

    return wrapper


@my_decorator
def my_func(t):
    sleep(t)
    print(f'sleep for {t} seconds')


def main():
    my_func(3)


if __name__ == '__main__':
    main()
