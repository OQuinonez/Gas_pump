import time
from gas_core import price_of_gas as price
from gas_core import calc_money as dinero
from gas_core import calc_gallon as gal
# from gas_core import diff_gas as gas

def main():

    print("Hello, welcome to O's station.\n")
    print("Here is the type of gas we have today.\n")
    with open('prices.txt', 'r') as file:
        list_gas = file.read()
        print(list_gas)
    type_gas = input("What type of gas would you like? \n\n")
    price_gas = price(type_gas)
    # diff_price = gas(type_gas)


        
    print("We have two different ways you can pay.\n")
    print("Prepay\n")
    print("or\n")
    print("After filling up")
    pay_type = input("How would you like to pay? \n")
    if pay_type.lower() == "prepay":
        print("Thanks for choosing Prepay.")
        money = input("How much money would you like to spend? \n")
        print("Press Enter to start filling")
        input()
        time.sleep(.5)
        print("You have bought", gal(money, price_gas), "gallons." )
    else:
        print("Thanks for choosing after filling up.\n")
        gallons = input("How many gallons would you want? \n")
        print("Press Enter to start filling")
        input()
        time.sleep(.5)
        print("Your total will be $", dinero(float(gallons), float(price_gas)))
    
if __name__ == '__main__':
    main()