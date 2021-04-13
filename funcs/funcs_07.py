# Создать функцию, которая принимает на вход
# неопределенное количество именованных аргументов и
# выводит на экран те из них, длина ключа которых четна.

def func(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(f'{key}: {value}')


def main():
    func(a=1, ad=2, asd=3, asdf=4, asdfg=5)


if __name__ == '__main__':
    main()
