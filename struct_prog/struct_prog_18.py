# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]


dict = {}
for i in range(200, 300):
    result_sum = 0
    for j in range(1, i - 1):
        if i % j == 0:
            result_sum += j
    dict[i] = result_sum

dict_result = {}
for key in dict.keys():
    for key_in_val in dict.keys():
        if key == dict[key_in_val]:
            if key_in_val == dict[key]:
                dict_result[key] = key_in_val

print(dict_result)
