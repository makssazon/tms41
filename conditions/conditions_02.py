# Ввести предложение. Если в предложении есть слово
# code - вывести на экран Yes, иначе вывести на экран No

my_str = input("enter str - ")

if "code" in my_str:
    print("yes")
else:
    print("no")

print("yes") if "code" in my_str else print("no")
