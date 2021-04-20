# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева
# направо и справа налево. (Определить функцию,
# позволяющую распознавать слова палиндромы.)[03-10.32]

def func_polindrom(word: str) -> bool:
    return word[::-1].lower() == word.lower()


def func(arr: list) -> bool:
    for word in arr:
        if func_polindrom(word):
            return True
    return False


def main():
    arr = ['alla', "Вадим", "абраарбА"]
    print(func(arr))


if __name__ == '__main__':
    main()
