# Создать файл sqlalchemy_04.py.
# Написать программу: пользователь вводит данные о книге.
# Пользователю отображается введенная им информация.
# Пользователю задается вопрос: “Хотите сохранить эту книгу?”.
# Если ответ да - выполнить метод .commit(), иначе - .rollback()

from sqlalchemy import create_engine


def book_add():
    id = int(input('id: '))
    title = input('title: ')
    pages = int(input('pages: '))
    author = input('author: ')
    price = float(input('price: '))
    release_year = int(input('release_year: '))
    e = create_engine('sqlite:///sa_test.db')
    conn = e.connect()
    trans = conn.begin()
    conn.execute("insert into book (id, title, pages,"
                 "author, price, release_year)"
                 "values (:id, :title, :pages, "
                 ":author, :price, :release_year)",
                 id=id, title=title, pages=pages,
                 author=author, price=price, release_year=release_year)
    choise_trans = input(f'do you want to save book with '
                         f'id={id}, title={title}, pages={pages}, '
                         f'author={author}, price={price},'
                         f' release_year={release_year} \n'
                         f'press y to save, something else for no: ')
    if choise_trans in 'yY':
        trans.commit()
    else:
        trans.rollback()
    conn.close()


def main():
    book_add()


if __name__ == '__main__':
    main()
