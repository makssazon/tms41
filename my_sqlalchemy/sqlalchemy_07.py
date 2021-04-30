# Создать файл sqlalchemy_07.py.
# Получить все книги и вывести их на экран в формате
# год - название - автор
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapper

from my_sqlalchemy.book import Book
from my_sqlalchemy.sqlalchemy_05 import book_table

e = create_engine('sqlite:///book.db', echo=True)
Session = sessionmaker(bind=e)
session2 = Session()
mapper(Book, book_table)

data = session2.query(Book)
for book in data:
    print(book.release_year, book.title, book.author)
