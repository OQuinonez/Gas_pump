def price_of_gas(type_gas):
    """(str) -> float
    This function will print a message to the user
    and return the float value of the price per gallon
    >>> price_of_gas('Regular')
    You picked Regular which is $ 2.07
    2.07
    >>> price_of_gas('medium')
    You picked Medium which is $ 2.30
    2.3
    >>> price_of_gas('Premium')
    You picked Premium which is $ 2.35
    2.35
    """
    if type_gas.lower() == "regular":
        print("You picked Regular which is $ 2.07")
        return 2.07
    elif type_gas.lower() == "medium":
        print("You picked Medium which is $ 2.30")
        return 2.30
    elif type_gas.lower() == "premium":
        print("You picked Premium which is $ 2.35")
        return 2.35
    else:
        return None



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


# def get_file(type_gas, gallons, money):
#     r = "Regular"
#     m = "Medium"
#     p = "Premium"

#     price = 


def main():
    if __name__ == '__main__':
        main()