# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
# [03-15.3]

with open('text_test.txt', 'w') as file:
    for i in range(1, 7):
        file.write(input(f'enter text for line {i} '))
        file.write('\n')

with open("text_test.txt") as file:
    print(file.read())
