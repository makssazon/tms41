# Написать игру. Пользователь должен угадать число.
# Сперва вводиться диапазон угадывания. После колличество попыток.
# В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или
# меньше искомое число). Если за указанное количество попыток
# число не угадано - выводить: You are the loser и правильное число.
from random import randint

first_num = int(input("enter first - "))
last_num = int(input("enter last - "))
num_try = int(input("number of attempts - "))

result = randint(first_num, last_num)
attempt = 1
while True:
    num_attempt = int(input(f'attempt {attempt}, enter number : '))
    attempt += 1
    if attempt > num_try + 1:
        print(f'You are the loser, правильное число : {result}')
        break
    if result == num_attempt:
        print('You are the winner.')
        break
    elif result > num_attempt:
        print('result > of your number')
    elif result < num_attempt:
        print('result < of your number')
