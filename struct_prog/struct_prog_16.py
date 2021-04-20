# Написать программу, в которой вводятся два операнда Х и Y и
# знак операции sign (+, –, /, *). Вычислить результат Z в
# зависимости от знака. Предусмотреть реакции на возможный
# неверный знак операции, а также на ввод Y=0 при делении.
# Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл).
# В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').


while True:
    sign = (input("enter sign, for out enter 0 - "))
    if sign == 0:
        break
    elif sign not in '+-/*':
        print("sign must be +,-,* or * ")
        continue
    x = float(input("enter x - "))
    y = float(input("enter y - "))
    if sign == '/':
        if y == 0:
            print("zero division error")
            continue
        z = x / y
    elif sign == '*':
        z = x * y
    elif sign == '+':
        z = x + y
    else:
        z = x - y
    print(f'result of {x} {sign} {y} = {z}')
