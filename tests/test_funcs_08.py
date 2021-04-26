from funcs.funcs_08 import avg_geom, avg_arifm, func


def test_avg_g():
    result = avg_geom((2, 2, 2))
    assert result == 2


def test_avg_a():
    result = avg_arifm((2, 2, 2, 4))
    assert result == 2.5


def test_main_func_geo():
    result = func(2, 2, 2, mean_type='geo')
    assert result == 2


def test_main_func_arif():
    result = func(2, 2, 2, 4, mean_type='arif')
    assert result == 2.5
