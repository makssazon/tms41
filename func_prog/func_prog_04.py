# Дан словарь, создать новый словарь,
# поменяв местам ключ и значение

dict = {'one': 1, 'two': 2, 'three': 3}
new_dict = {value: key for key, value in dict.items()}
print(new_dict)
