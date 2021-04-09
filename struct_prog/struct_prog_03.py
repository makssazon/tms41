# Получить на ввод количество рублей и копеек и вывести
# в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки

price = input('enter price - ')

arr_price = price.split('.')
if len(arr_price) > 1:
    rubl = int(arr_price[0])
    cent = int(arr_price[1])
    if rubl and cent:
        print(f'{rubl} рубля {cent} копеек')
    else:
        print(f'{cent} копеек')
else:
    print(f'{arr_price[0]} рублей')
