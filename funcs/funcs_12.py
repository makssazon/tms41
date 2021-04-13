def my_func(a: int, b: float) -> str:
    c = f'{a}{b}'
    print(c)
    return c


print(type(my_func(1, 1.2)))
