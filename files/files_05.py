# Имеется текстовый файл. Все четные строки этого
# файла записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.
# [03-15.29]

with open('text_test.txt') as file:
    with open('text_05_1.txt', 'w') as file_1:
        with open('text_05_2.txt', 'w') as file_2:
            i = 1
            while line := file.readline():
                if i % 2:
                    file_2.write(line)
                else:
                    file_1.write(line)
                i += 1

with open('text_05_1.txt') as file:
    print(file.read())
print()
with open('text_05_2.txt') as file:
    print(file.read())
