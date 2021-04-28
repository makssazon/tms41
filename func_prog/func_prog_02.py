# Дан список слов.
# Сгенерировать новый список с перевернутыми словами

arr = ['asdf', 'qwer', 'zxcv', 'qwer']

arr_new = [word[::-1] for word in arr]
print(arr_new)
