# Написать скрипт - таймер. Программа при запуске принимает
# имя, фамилию, часы, минуты и секунды.
# После программа начинает обратный отсчет выводя оставшееся время.
# Программа должна хранить файл логирования с информацией
# о том кто запускал программу и когда.
# Пример:
# 00:00:03
# 00:00:02
# 00:00:01
# ALARM!!!
import csv
import os
import time
from datetime import timedelta
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name')
parser.add_argument('-ln', '--last_name')
parser.add_argument('-hr', '--hours', default=0)
parser.add_argument('-m', '--minutes', default=0)
parser.add_argument('-s', '--seconds')
args = parser.parse_args()
delta_time = timedelta(hours=int(args.hours),
                       minutes=int(args.minutes),
                       seconds=int(args.seconds))
time_start = time.ctime()

if not os.path.exists('log_timer.csv'):
    with open('log_timer.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        fields = ['first name', 'last name', 'time start']
        csvwriter.writerow(fields)

with open('log_timer.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    arr = [args.first_name, args.last_name, time_start]
    csvwriter.writerow(arr)

second = timedelta(seconds=1)
end_time = timedelta(seconds=0)
while delta_time >= end_time:
    print(delta_time)
    delta_time -= second
    time.sleep(1)
print('time was ended')
