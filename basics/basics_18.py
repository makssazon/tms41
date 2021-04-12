# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы.

my_str = "улыбок тебе дед макар"
new_my_str = my_str.split(' ')
new_my_str.reverse()
result = " ".join(new_my_str)
print(result)
