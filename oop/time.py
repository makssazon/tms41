# Создать файл time.py. Создать класс MyTime.
# Атрибуты: hours, minutes, seconds.
# Переопределить магические методы сравнения(равно, не равно),
# сложения, вычитания, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида:
# одна строка, три числа, другой объект класса MyTime.
# В остальных случаях создавать объект по-умолчанию(0-0-0)


class MyTime:
    def __init__(self, *args):
        if not any(args):
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif type(args[0]) == str:
            args = args[0].split()
            self.hours = int(args[0])
            self.minutes = int(args[1])
            self.seconds = int(args[2])
        elif type(args[0]) == int:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif type(args[0]) == type(self):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds

    def __str__(self):
        return f'{self.hours} hours {self.minutes} ' \
               f'minutes {self.seconds} seconds'

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) \
               == (other.hours, other.minutes, other.seconds)

    def __ne__(self, other):
        return not (self.hours, self.minutes, self.seconds) \
                   == (other.hours, other.minutes, other.seconds)

    def __add__(self, other):
        seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        delta_seconds = seconds_self + seconds_other
        m, s = divmod(delta_seconds, 60)
        h, m = divmod(m, 60)
        return MyTime(h, m, s)

    def __sub__(self, other):
        seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        delta_seconds = seconds_self - seconds_other
        m, s = divmod(delta_seconds, 60)
        h, m = divmod(m, 60)
        return MyTime(h, m, s)


t = MyTime()
print(t.hours, t.minutes, t.seconds)
t2 = MyTime('00 10 00')
print(t2.hours, t2.minutes, t2.seconds)
t3 = MyTime(t2)
print(t3.hours, t3.minutes, t3.seconds)
t4 = MyTime(11, 59, 0)
print(t4.hours, t4.minutes, t4.seconds)
print(t2 == t3)
print(t != t3)
t_plus = t2 + t2
print(t_plus)
t_minus = t4 - t2
print(t_minus)
