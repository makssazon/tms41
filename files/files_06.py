# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки. Если нет,
# то получить номер первой строки, в которой
# эти файлы отличаются друг от друга.
# [03-15.31]


with open('text_test.txt') as file_1:
    with open('text_05_2.txt') as file_2:
        i = 0
        while line := file_1.readline():
            if not line == file_2.readline():
                print(f'diferent on line # {i}')
                break
            i += 1
