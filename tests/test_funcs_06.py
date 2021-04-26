from funcs.funcs_06 import func


def test_summ_max_args():
    result = func(1, 2, 3)
    assert result == (6, 3)


def test_summ_max_args_1():
    result = func(1, 2, 3, -10)
    assert result == (-4, 3)
