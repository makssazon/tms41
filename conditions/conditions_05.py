# Ввести число, проверить на то, что было введено
# именно число. Возвести его в куб и вывести результат на экран.

my_num = input('enter number - ')

if my_num.isdigit():
    print(float(my_num) ** 3)
else:
    print("wrong input")
