# Запросить у пользователя возраст.
# Если возраст меньше 0 - вывести Wrong input,
# если меньше 18 - вывести CocaCola, иначе - вывести Beer

age = int(input("enter your age - "))

if age < 0:
    print("wrong input")
elif age < 18:
    print("cola")
else:
    print("beer")

print("wronge") if age < 0 else print("cola") if age < 18 else print("beer")
