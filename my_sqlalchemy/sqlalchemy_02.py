# Создать файл sqlalchemy_02.py. Создать соединение к
# базе sa_test.db. Создать 5 книг с помощью sqlalchemy.
from sqlalchemy import create_engine

e = create_engine('sqlite:///sa_test.db')
e.execute("""
            insert into Book values
            (1,'master', 380, 'Bulgakov', 25, 1965),
            (2, 'harry', 600, 'Rolling', 35, 2001),
            (3, 'skot', 300, 'Oryel', 30, 1956),
            (4, 'norvegian wood', 200, 'murakami', 40, 1995),
            (5, 'dva kapitana', 500, 'kaverin', 20, 1955)
""")
