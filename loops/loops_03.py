# Просуммировать неопределенное количество чисел,
# вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп»

result = 0
while True:
    num = input("enter number, for stop enter stop - ")
    if "stop" in num:
        break
    result += float(num)
print(result)
