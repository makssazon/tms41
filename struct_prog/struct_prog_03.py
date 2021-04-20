# Получить на ввод количество рублей и копеек и вывести
# в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки

rubli = input('enter rubli : ')
cents = input('enter cents : ')
if len(rubli) > 1:
    if rubli[-1] == "1" and rubli[-2] != "1":
        count_rubli = 'рубль'
    elif rubli[-2] == '1' or rubli[-1] in '56789' or rubli[-1] == '0':
        count_rubli = 'рублей'
    else:
        count_rubli = 'рубля'
else:
    if rubli == '1':
        count_rubli = 'рубль'
    elif rubli in '234':
        count_rubli = 'рубля'
    else:
        count_rubli = 'рублей'

if len(cents) > 1:
    if cents[-1] == "1" and cents[-2] != "1":
        count_cents = 'копейка'
    elif cents[-2] == '1' or cents[-1] in '56789' or cents[-1] == '0':
        count_cents = 'копеек'
    else:
        count_cents = 'копейки'
else:
    if cents == '1':
        count_cents = 'копейка'
    elif cents in '234':
        count_cents = 'копейки'
    else:
        count_cents = 'копеек'

if rubli and cents:
    print(f'{rubli} {count_rubli}, {cents} {count_cents}')
