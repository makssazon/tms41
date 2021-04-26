# Написать функции по работе с csv файлами в файле csv_utils.py.
# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец)
# Удаление записи(по позиции, по-умолчанию последнюю).
# В файле files_08 импортировать функции.
# С помощью функций создать файл с информацией о товарах
# (Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
from files.csv_utils import create, read, add, delete


def main():
    fields = ['имя товара', 'цена', 'количество', 'комментарий']
    rows = [['хлеб', 2, 1, 'best bread'],
            ['potatos', 3, 5, 'best potatos'],
            ['beer', 2, 15, 'best beer']]
    create("test.csv", fields, rows)
    print(read("test.csv"))
    row = ['wisky', 50, 2, 'best wisky']
    add('test.csv', row, 1)
    print()
    print(read('test.csv'))
    delete('test.csv', 3)
    print()
    print(read('test.csv'))


if __name__ == '__main__':
    main()
