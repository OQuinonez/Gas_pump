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
def subtracting_tank(inventory, type_gas, gallons):
    """ [[str, float, float]], gallons -> list[list]
    return inventory with the differnce after 
    the gallons bought
    """
    updated_inventory = []
    for i in inventory:
        i[0] = str(i[0])
        i[1] = str(i[1])
        i[2] = float(i[2])
        if type_gas == i[0].lower():
            diff = i[2] - float(gallons)
        else:
            diff = i[2]

    message = type_gas + ', ' + str(gallons)
    with open('prices.txt', 'a') as f:
        updated_inventory.append([i[0], i[1], diff])
    return updated_inventory

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