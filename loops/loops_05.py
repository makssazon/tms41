# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел
# от 1 до n(включая n) используя цикл while

num = int(input("enter num - "))
result = 0
while num:
    result += num ** 3
    num -= 1
print(result)
