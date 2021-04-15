# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.
# [03-15.16]


file = open('/home/tms/PycharmProjects/text.txt')
file_arr = file.readlines()
print(file_arr[0])
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

file = open('/home/tms/PycharmProjects/text.txt')
while line := file.readline():
    print(line)
