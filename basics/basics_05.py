# Ввести предложение состоящее из двух слов.
# Поменять местами слова, добавить восклицательный знак в начало и
# конец, вывести итоговое предложение на экран.

my_str = 'abra kadabra'
new_my_str = my_str.split()
new_my_str.append("!")
new_my_str = new_my_str[::-1]
new_my_str.append("!")
result = " ".join(new_my_str)
print(result)
