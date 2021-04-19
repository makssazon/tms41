# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл
import json
from random import randint

matrix = [[randint(1, 10) for i in range(4)] for row in range(4)]
print(matrix, type(matrix))

with open('text_07.txt', 'w') as file:
    data = json.dumps(matrix)
    print(type(data))
    file.write(data)

with open('text_07.txt') as file:
    data = json.loads(file.read())
    print(data, type(data))
    index = 1
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            if not index % 2:
                data[i][j] = None
            index += 1
    with open('text_07_1.txt', 'w') as file_2:
        json.dump(data, file_2)

with open('text_07_1.txt') as file:
    data = json.loads(file.read())
    print(data, type(data))
