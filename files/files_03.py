# В конец существующего текстового файла
# записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
# [03-15.6]

with open('text_test.txt', 'a') as file:
    while True:
        line = input('enter line, for exit enter 0 : ')
        if line == '0':
            break
        else:
            file.write(line)
            file.write('\n')

with open('text_test.txt') as file:
    print(file.read())
