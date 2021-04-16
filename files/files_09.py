# Использовать результаты files_08. Все функции описываются в csv_utils.py.
# Проверка работы функции осуществляется в files_09.py.
# Создать функцию подсчета полной суммы всех товаров.
# Создать функцию поиска самого дорогого товара.
# Создать функцию самого дешевого товара.
# Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
from files.csv_utils import summa, max_price, min_price, minus, read


def main():
    read('test.csv')
    summa('test.csv')
    print()
    max_price('test.csv')
    min_price('test.csv')
    minus('test.csv', 3)
    print()
    read('test.csv')


if __name__ == '__main__':
    main()
