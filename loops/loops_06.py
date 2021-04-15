# Написать программу, которая будет выводить
# на экран случайные числа от 1 до 10 до тех пор,
# пока не выпадет 7.
from random import randint

num = 0
while num != 7:
    num = randint(1, 10)
    print(num)
print("end - num is 7")
