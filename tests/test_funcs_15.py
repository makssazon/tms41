from funcs.funcs_15 import fact2


def test_fact2():
    result = fact2(5)
    assert result == 15


def test_fact2_1():
    result = fact2(4)
    assert result == 8
