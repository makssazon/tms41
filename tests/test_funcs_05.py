from funcs.funcs_05 import func


def test_sum_arg_times_i():
    result = func(4, 3, 2, 1)
    assert result == 10


def test_sum_arg_times_i_1():
    result = func(1)
    assert result == 0
