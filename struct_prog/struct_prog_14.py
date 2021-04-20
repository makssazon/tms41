# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
#
# предоставить 2 решения. Одно с использованием цикла while,
# другое с использованием цикла for с параметром.
# Оба решения предоставить в одном файле.

arr = [i for i in range(1, 7)]
print(arr)

new_arr = []
for i in arr[1:]:
    new_arr.append(i)
new_arr.append(arr[0])
print(new_arr)

new_arr_2 = []
while len(arr) > 1:
    new_arr_2.append(arr.pop(1))
else:
    new_arr_2.append(arr[0])
print(new_arr_2)
