# Дан словарь: {'test': 'test_value', 'europe': 'eur',
# 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
# получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
# предоставить 2 решения. Одно с использованием цикла while, другое с
# использованием цикла for с параметром.
# Оба решения предоставить в одном файле.

# 1
dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = list(dict.keys())
for key in keys:
    dict[key + str(len(key))] = dict.pop(key)
print(dict)

# 2
dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = [key for key in dict.keys()]
dict_2 = {}
print(keys)

i = 0
while dict:
    dict_2[keys[i] + str(len(keys[i]))] = dict.pop(keys[i])
    i += 1
print(dict_2)
