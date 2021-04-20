# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]
from random import randint

arr = [randint(1, 20) for i in range(19)]
print(arr, len(arr))
result = 0
flag = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        if flag:
            result += 1
            flag = False
    else:
        flag = True
print(result)
