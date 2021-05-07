# Создать файл sqlalchemy_08.py.
# Написать программу: пользователь вводит границы
# фильтрации по году. Отобразить на экране те книги,
# год которых находиться в заданных границах.
# Если таких книг нет - вывести сообщение: Not foun
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker, mapper

from my_sqlalchemy.book import Book
from my_sqlalchemy.sqlalchemy_05 import book_table


def filter_year(start, finish):
    e = create_engine('sqlite:///book.db', echo=True)
    session = sessionmaker(bind=e)()
    mapper(Book, book_table)
    result = session.query(Book).filter(and_(Book.release_year > start,
                                             Book.release_year < finish))
    return result


def main():
    start_year = int(input('enter start year: '))
    finish_year = int(input('enter end of period: '))
    result = list(filter_year(start_year, finish_year))
    if len(result) > 0:
        for book in result:
            print(book.title, book.author, book.release_year)
    else:
        print('Not found')


if __name__ == '__main__':
    main()
