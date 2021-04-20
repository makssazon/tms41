from funcs.funcs_09 import func


def test_count_element_arr():
    result = func([1, 2, 1, 1])
    assert result == {1: 3, 2: 1}
