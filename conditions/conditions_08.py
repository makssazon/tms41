# Ввести почтовый адрес. Проверить доменной имя.
# В случае если оно gmail.com, вывести на экран
# имя почтового ящика. Иначе вывести надпись
# “DOMAIN NAME is not supported’

mail = input("enter email - ")

if 'gmail.com' in mail:
    print(mail)
else:
    print("DOMAIN NAME is not supported")
