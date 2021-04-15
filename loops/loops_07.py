# Получить сумму кубов натуральных чисел
# от n до m используя цикл for

n = int(input('enter n - '))
m = int(input('enter m - '))

print(sum([i ** 3 for i in range(n, m)]))
