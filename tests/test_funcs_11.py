from funcs.funcs_11 import func


def test_func_0():
    result = func(5, 3, 7)
    assert result == (0, 0)


def test_func_1():
    result = func(1, -2, -3)
    assert result == (3, -1)


def test_func_2():
    result = func(1, 12, 36)
    assert result == (-6, -6)
