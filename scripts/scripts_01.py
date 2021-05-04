# Создать скрипт, который при запуске принимает неопределенное
# количество аргументов и считает сумму тех из них, что являются цифрами.
# Пример:
# python test.py 1 2 3 4 a b 5 6 -->  21

import sys

print(sys.argv)
digits = sum(map(float, (filter(lambda x: x.isdigit(), sys.argv))))
print(digits)
