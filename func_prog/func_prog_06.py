# Дан список имен, отфильтровать все имена, где есть буква o
#
# [‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]

arr = ['Kate', 'Kolya', 'Alex', 'VanO']
new_arr = list(filter(lambda x: 'o' in x.lower(), arr))
print(new_arr)
