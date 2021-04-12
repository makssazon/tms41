# Пользователь вводит три числа. Увеличьте первое число в два раза,
# второе числа уменьшите на 3, третье число возведите в квадрат
# и затем найдите сумму новых трех чисел.

num_1 = int(input("enter number 1 - "))
num_2 = int(input("enter number 2 - "))
num_3 = int(input("enter number 3 - "))
print(f"result of magic script - {num_1 * 2 + num_2 - 3 + num_3 ** 2}")
