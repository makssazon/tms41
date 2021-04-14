# Описать функцию is_power_n( k , n ) логического типа, возвращающую
# True, если целый параметр k (> 0) является степенью числа n (> 1), и False
# в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
# ных чисел. С помощью функции is_power_n найти количество степеней чис-
# ла N в данном наборе.
# [01-11.2-Proc27]
import math


def my_func(k: int, n: int) -> bool:
    result = math.log(k, n)
    print(result)
    return True if int(result) == result else False


def main():
    arr = [1, 5, 3, 36, 27, 81, 108, 243, 502, 729]
    result = 0
    for i in arr:
        if my_func(i, 3):
            result += 1
    print(result)


if __name__ == '__main__':
    main()
