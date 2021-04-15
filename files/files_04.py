# Имеется текстовый файл. Переписать в другой файл
# все его строки с заменой в них символа 0 на символ 1 и наоборот.

with open('text_test.txt') as file:
    file = file.read()
    with open('text_04.txt', 'w') as new_file:
        for letter in file:
            if letter == '0':
                new_file.write('1')
            elif letter == '1':
                new_file.write('0')
            else:
                new_file.write(letter)

with open('text_04.txt') as file:
    print(file.read())
