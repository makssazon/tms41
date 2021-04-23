class MyExeption_int_must_be(Exception):
    def __init__(self, message='pages and year must be int'):
        super().__init__(message)


class MyExeption_str_must_be(Exception):
    def __init__(self, message='author must be str'):
        super().__init__(message)


class MyExeption_int_or_float_must_be(Exception):
    def __init__(self, message='price must be int or float'):
        super().__init__(message)


class Book:
    def __init__(self, pages: int, year: int,
                 author: str, price: float or int):
        if not isinstance(pages, int) or not isinstance(year, int):
            raise MyExeption_int_must_be
        if not isinstance(author, str):
            raise MyExeption_str_must_be
        if not isinstance(price, (int, float)):
            raise MyExeption_int_or_float_must_be
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price


def main():
    try:
        Book(20, 'df', 'igar', 'hjg')
    except MyExeption_int_must_be as err:
        print(f'Problem with int - {err}, object was not create')
    except MyExeption_str_must_be as err:
        print(f'Problem with args str- {err}, object was not create')
    except MyExeption_int_or_float_must_be as err:
        print(f'Problem with int or float - {err}, object was not create')
    else:
        print('object was created')
    finally:
        print('for create book input pages: int, year: '
              'int, author: str, price: float or int')


if __name__ == '__main__':
    main()
