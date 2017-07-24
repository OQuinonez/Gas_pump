import gas_core
def test_calc_gallon():
    assert gas_core.calc_gallon(0, 2.07) == 0.0
    assert gas_core.calc_gallon(20, 2.07) == 41.4
    assert gas_core.calc_gallon(1, 2.07) == 2.07
def test_calc_money():
    assert gas_core.calc_money(1, 2.07) == 2.07
    assert gas_core.calc_money(20, 2.07) == 41.4
    assert gas_core.calc_money(10, 2.07) == 20.7

def test_final_message():
    actual =  gas_core.final_message('regular', 2.05, 12)
    expected = 'You bought 12.00 gallons of regular gas for $2.05.'
    assert actual == expected

# def test_other_message():

#     # For paying after
#     """ str, float, float -> str """
#     return 'Your total is ${:0.2f} of {} gas for {} gallons.'.format(gallons, name, price)