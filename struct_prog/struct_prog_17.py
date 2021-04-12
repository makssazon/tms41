# Дано число. Найти сумму и произведение его цифр.
from functools import reduce

num = input('enter number : ')

result_sum = sum(list(map(lambda x: int(x), num)))
result_mult = reduce(lambda x, y: x * y, list(map(lambda x: int(x), num)))

print(f'result sum : {result_sum}, result mult : {result_mult}')
