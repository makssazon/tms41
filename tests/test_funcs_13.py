from funcs.funcs_13 import func


def test_sum_negativ_i_positiv_of_arr():
    result = func([1, 1, -1, -2, 3])
    assert result == (-3, 5)
