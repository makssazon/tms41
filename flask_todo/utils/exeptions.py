class MyException(Exception):
    def __init__(self, message='ParentException'):
        super().__init__(message)


class NoUserOrPSW(MyException):
    def __init__(self, message='NoUserOrPSW'):
        super().__init__(message)


class NoLink(MyException):
    def __init__(self, message='NoLink'):
        super().__init__(message)
