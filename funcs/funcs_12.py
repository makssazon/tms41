# Описать функцию is_power_n( k , n ) логического типа, возвращающую
# True, если целый параметр k (> 0) является степенью числа n (> 1), и False
# в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
# ных чисел. С помощью функции is_power_n найти количество степеней чис-
# ла N в данном наборе.
# [01-11.2-Proc27]


def my_func(k: int, n: int) -> bool:
    i = 0
    while True:
        n_in_i = n ** i
        if k == n_in_i:
            return True
        elif k < n_in_i:
            return False
        i += 1


def main():
    arr = [1, 5, 3, 36, 27, 81, 108, 243, 502, 729]
    result = 0
    for i in arr:
        if my_func(i, 3):
            result += 1
    print(result)


if __name__ == '__main__':
    main()
