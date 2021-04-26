from funcs.funcs_04 import func


def test_matrix():
    result = len(func(2))
    assert result == 2


def test_matrix_0():
    result = len(func(0))
    assert result == 0
