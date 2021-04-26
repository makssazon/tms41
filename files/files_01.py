# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.
# [03-15.16]


file = open('/home/tms/PycharmProjects/text.txt')
fileread = file.read()
arr = fileread.split('\n')
print(arr[0], arr[4], '\n'.join(arr[:5]),
      '\n'.join(arr[0:2]), '\n'.join(arr), sep='\n\n')
file.close()

# a) его первую строку;
file = open('/home/tms/PycharmProjects/text.txt')
print(file.readline())
file.close()

# b) его пятую строку;
file = open('/home/tms/PycharmProjects/text.txt')
i = 0
while line := file.readline():
    if i == 4:
        print(line)
        break
    i += 1
file.close()

# c) его первые 5 строк;
file = open('/home/tms/PycharmProjects/text.txt')
i = 0
while line := file.readline():
    if i < 4:
        print(line)
    else:
        break
    i += 1
file.close()

# d) его строки с s1-й по s2-ю;
file = open('/home/tms/PycharmProjects/text.txt')
i = 0
while line := file.readline():
    if 0 <= i < 2:
        print(line)
    elif i > 2:
        break
    i += 1
file.close()

# e) весь файл.
file = open('/home/tms/PycharmProjects/text.txt')
while line := file.readline():
    print(line)
file.close()

file = open('/home/tms/PycharmProjects/text.txt')
file_arr = file.readlines()
print(file_arr[0], type(file_arr), type(file_arr[0]))
print(file_arr[4])
for line in file_arr[:5]:
    print(line.strip())
print()
for line in file_arr[1:3]:
    print(line.strip())
print()
for line in file_arr:
    print(line.strip())
file.close()
