# Введите число. Если это число делиться на 1000 без остатка,
# то выведите на экран "millennium"

num = float(input('enter number : '))
if not num % 10e3:
    print('millennium')
