def load_inventory():
    """ -> list[list]
    returns inventory
    """
    with open("prices.txt", 'r') as file:
        file.readline()
        items = file.readlines()
    inventory = []
    for element in items:
        pieces = element.split(', ')
        inventory.append([pieces[0], float(pieces[1].strip()), float(pieces[2].strip())])
    return inventory

def price_of(inventory, gas_name):
    ''' ([[str, float, float]], str) _> (float)
    This function will get a string and 
    it will look in a txt file and pull out 
    the price of that gas and return it
    ''' 
    for item in inventory:
        if gas_name.strip() == item[0].strip().lower():
            return float(item[1])

def just_price(type_gas, gallons):
    '''
    Gets the price of each gas type.

    >>> just_price('regular', 18)
    37.26
    >>> just_price('medium', 13)
    29.9
    >>> just_price('premium', 14)
    32.9
    '''
    if type_gas.lower() == "regular":
        return 2.07 * gallons
    elif type_gas.lower() == "medium":
        return 2.30 * gallons
    elif type_gas.lower() == "premium":
        return 2.35 * gallons
    else:
        return None

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



def subtracting_tank(inventory, gallons):
    """ [[str, float, float]] -> list[list]
    return inventory with the differnce after 
    the gallons bought
    """
    updated_inventory = []
    for i in inventory:
        i[0] = str(i[0])
        i[1] = str(i[1])
        i[2] = float(i[2])
        diff = i[2] - gallons
        n = 5000 - diff
        if diff <= n:
            diff+= n
        update_inventory.append(i[0], i[1], i[2])
    return updated_inventory