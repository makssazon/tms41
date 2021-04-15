# Просуммировать неопределенное количество чисел, вводимых
# пользователем, суммировать до тех пор, пока пользователь
# не введёт слово «стоп». Не учитывать числа кратные 5

result = 0
while True:
    num = input("enter number, for stop enter stop - ")
    if "stop" in num:
        break
    num = float(num)
    if num % 5 == 0:
        continue
    result += num
print(result)
