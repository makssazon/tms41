from funcs.funcs_17 import fact, func


def test_fact_sin():
    result = fact(3)
    assert result == 6


def test_func_sin():
    result = func(1, 0)
    assert result == 0.8414709848078965
