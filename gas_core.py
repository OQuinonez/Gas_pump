from disk import subtracting_tank, load_inventory
def price_of(inventory, gas_name):
    ''' ([[str, float, float]], str) _> (float)
    This function will get a string and 
    it will look in a txt file and pull out 
    the price of that gas and return it
    ''' 
    for item in inventory:
        if gas_name.strip() == item[0].strip().lower():
            return float(item[1])



def calc_gallon(money, price_gas):
    """ (float, float) _> float
    This funciton will get the amount of money
    and it will return the amount of gallons
    >>> calc_gallon(0, 2.07)
    0.0
    >>> calc_gallon(20, 2.07)
    41.4
    >>> calc_gallon(1, 2.07)
    2.07
    """
    answer = (money * price_gas)
    return answer

def calc_money(gallons, price_gas):
    ''' (float,float) _> float
    This function will get the amount of gallons 
    and it will return the amount of money spent
    >>> calc_money(1, 2.07)
    2.07
    >>> calc_money(20, 2.07)
    41.4
    >>> calc_money(10, 2.07)
    20.7
    '''
    answer = (gallons * price_gas)
    return answer


def update_inventory(type_gas, gallons, price):
    ''' str, float, float _> None
    '''
    msg = type_gas + ', ' + str(gallons) + ', ' + str(price) + '\n'
    with open('gas.txt', 'a') as file:
        file.write(msg)
    return None
def final_message(name, price, gallons):
    # for prepay
    """ str, float, float -> str """
    return 'You bought {:0.2f} gallons of {} gas for ${:0.2f}.'.format(gallons, name, price)
def other_message(name, price, gallons):

    # For paying after
    """ str, float, float -> str """
    return 'Your total is ${:0.2f} of {} gas for {} gallons.'.format(gallons, name, price)
def manager_inventory():
    ''' _> dict{dict{}}
    Fuction will load the prices as a dictionaries of 
    dictionaries.
    '''
    inventory = {}
    with open('prices.txt', 'r') as file:
        _, key_1, key_2, key_3 = file.readline().strip().split(', ')
        lines = file.readlines()
        for line in lines:
            gas_type, price, gallons, code = line.strip().split(', ')
            inventory[gas_type] = {key_1: float(price), key_2: float(gallons), key_3: str(code)}
        return inventory