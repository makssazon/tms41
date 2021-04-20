from funcs.funcs_12 import my_func


def test_log_0():
    result = my_func(3, 9)
    assert result is False


def test_log_1():
    result = my_func(9, 3)
    assert result is True
