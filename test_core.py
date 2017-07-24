import gas_core
def test_calc_gallon():
    assert gas_core.calc_gallon(0, 2.07) == 0.0
    assert gas_core.calc_gallon(20, 2.07) == 41.4
    assert gas_core.calc_gallon(1, 2.07) == 2.07
def test_calc_money():
    assert gas_core.calc_money(1, 2.07) == 2.07
    assert gas_core.calc_money(20, 2.07) == 41.4
    assert gas_core.calc_money(10, 2.07) == 20.7