# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести
# все сведения о поездах, время пребывания в пути
# которых превышает 7 часов 20 минут.[02-7.3-ML02]
# Примечание: данное задание подразумевает самостоятельное
# изучение принципов работы со временем в Python(библиотека datetime)
from datetime import timedelta, datetime

dict = [{'number': 1,
         'station_arrive': 'Minsk',
         'time_arrive': datetime(2021, 4, 12, 8, 30),
         'station_start': 'Moskow',
         'time_start': datetime(2021, 4, 11, 21, 30)},

        {'number': 2,
         'station_arrive': 'Minsk',
         'time_arrive': datetime(2021, 4, 12, 15, 30),
         'station_start': 'Brest',
         'time_start': datetime(2021, 4, 12, 8, 30)},

        {'number': 3,
         'station_arrive': 'Minsk',
         'time_arrive': datetime(2021, 4, 12, 18, 20),
         'station_start': 'Vilnus',
         'time_start': datetime(2021, 4, 12, 16, 10)}

        ]

limit = timedelta(hours=7, minutes=20)

for train in dict:
    time_in_road = train['time_arrive'] - train['time_start']
    if time_in_road > limit:
        print(time_in_road, train)
