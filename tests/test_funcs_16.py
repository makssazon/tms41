from funcs.funcs_16 import func_polindrom, func


def test_polindrom():
    result = func_polindrom('adda')
    assert result is True


def test_polindrom_1():
    result = func_polindrom('addaa')
    assert result is False


def test_arr_polindrom():
    result = func(['alla', "Вадим", "абраарбА"])
    assert result is True


def test_arr_polindrom_1():
    result = func(['allaa', "Вадим", "абраарбАa"])
    assert result is False
