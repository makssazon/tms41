# Пользователь вводит время в минутах и
# расстояние в километрах. Найдите скорость в м/c.

time = float(input("enter time of road in minutes - "))
distance = float(input("enter distance of road in km - "))

print(f"speed in meters/second - {distance * 10 ** 3 / (time * 60)}")
