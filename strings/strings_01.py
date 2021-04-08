# Создать переменные firstname, lastname, age с соответствующими значениями
# Путем сложения получить строку вида
# Привет, меня зовут Иван Иванович, мне 35 лет
# Вывести на экран длину строки
# Примечание: переменную age задавать как строку ‘35’

firstname = "Abram"
lastname = "Abramovich"
age = "40"
result = "Hi, my name is " + firstname + " " + lastname + ', my age is ' + age
print(f"{result}, len of result is {len(result)}")
