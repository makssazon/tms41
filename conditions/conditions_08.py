# Ввести почтовый адрес. Проверить доменной имя.
# В случае если оно gmail.com, вывести на экран
# имя почтового ящика. Иначе вывести надпись
# “DOMAIN NAME is not supported’

mail = input("enter email - ")

index = mail.rindex('@')
if '@gmail.com' in mail[index:]:
    print(mail)
else:
    print("DOMAIN NAME is not supported - ", mail)

arr = mail.split('@')
if 'gmail.com' in arr[-1]:
    print(mail)
else:
    print("DOMAIN NAME is not supported - ", mail)
