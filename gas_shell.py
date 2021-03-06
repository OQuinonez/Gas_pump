import time
from disk import load_inventory, update_inventory
from gas_core import calc_money as dinero
from gas_core import calc_gallon as gal
from gas_core import price_of, final_message
from gas_core import other_message


def gas_function():
    print(
        "Hello, welcome to O's station.\n\nHere is the type of gas we have today.\n"
    )
    inventory = load_inventory()
    print(inventory)
    type_gas = input("What type of gas would you like? \n\n").lower().strip()
    print("\nIf you wish to exit press 'Q'\n")
    gas_price = price_of(inventory, type_gas)
    if not gas_price:
        print('That gas does not exist')
        exit()

    print("We have two different ways you can pay.\n")
    print("Prepay\n\nor\n\nAfter filling up")
    pay_type = input("How would you like to pay? \n")
    if pay_type.lower() == "prepay":
        print("Thanks for choosing Prepay.")
        money = input("How much money would you like to spend? \n")
        gallons = float(money) / float(gas_price)
        print("Press Enter to start filling")
        input()
        time.sleep(1.5)
        print(
            final_message(type_gas,
                          float(money), float(money) / float(gas_price)))
    elif pay_type.lower() == 'q':
        exit()
    else:
        print("Thanks for choosing after filling up.\n")
        gallons = input("How many gallons would you want? \n")
        money = float(gallons) * float(gas_price)
        print("Press Enter to start filling")
        input()
        time.sleep(1.5)
        print(
            other_message(type_gas,
                          float(gallons), float(gallons) * float(gas_price)))
    update_inventory(type_gas, gallons, money)


def main():
    gas_function()


if __name__ == '__main__':
    main()