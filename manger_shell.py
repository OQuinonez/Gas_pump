from gas_core import manager_inventory
from disk import subtracting_tank
print("Hello manager, here is our inventory")
inventory = manager_inventory()
print(inventory)
print('What would you like to do today?')
print('1.\tRefuel\n2.\tCheck the gallons bought for a specefic gas type\n3.\tCheck the amount of gas bought for the day')
answer = input().strip()
# if answer == '1':

