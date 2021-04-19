# Создать csv файл с данными о ежедневной погоде.
# Структура:  Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы)
# для Минск за последние 7 дней.
import csv
import datetime

arr = [['date', 'place', 'degrees', 'wind'],
       ['2021-04-10', 'minsk', 500, 1500],
       ['2021-04-11', 'minsk', 10, 15],
       ['2021-04-12', 'minsk', 5, 10],
       ['2021-04-13', 'minsk', 9, 11],
       ['2021-04-14', 'minsk', 15, 5],
       ['2021-04-15', 'minsk', 12, 7],
       ['2021-04-16', 'minsk', 14, 8],
       ['2021-04-17', 'minsk', 8, 20],
       ['2021-04-18', 'minsk', 8, 20],
       ['2021-04-19', 'minsk', 10, 20],
       ['2021-04-19', 'brest', 500, 1000],
       ]

delta_finish = datetime.datetime.now()
delta = datetime.timedelta(7)
delta_start = delta_finish - delta
print(delta_start, delta_finish, int(delta.days))

with open('test_11.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(arr)

with open('test_11.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]
    for row in rows[1:]:
        row[0] = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        row[2] = int(row[2])
        row[3] = int(row[3])
    total_degrees = 0
    total_wind = 0
    for row in rows[1:]:
        if delta_start <= row[0] < delta_finish and row[1] == 'minsk':
            total_degrees += row[2]
            total_wind += row[3]
    delta = int(delta.days)
    avg_degrees = total_degrees / delta
    avg_wind = total_wind / delta
    print(f'avg_degrees : {avg_degrees}, avg_wind : {avg_wind}')
