# Создать файл sqlalchemy_03.py.
# Написать программу: пользователь вводит год.
# Отобразить на экране те книги, год которых
# меньше введенного пользователем года. Если таких
# книг нет - вывести сообщение: Not found.
# Для проверки количества записей - привести
# результат запроса к списку и использовать функцию len()
from sqlalchemy import create_engine


def sql_finder_year():
    year = int(input("enter year to see books's year < your year : "))
    e = create_engine('sqlite:///sa_test.db')
    result = list(e.execute(f"""
                        select * from Book
                        where release_year<{year}
                        """))
    if len(result) > 0:
        for i in result:
            print(i)
    else:
        print('not found')


def main():
    sql_finder_year()


if __name__ == '__main__':
    main()
