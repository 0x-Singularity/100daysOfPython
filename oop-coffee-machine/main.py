from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

isOn = True

while isOn:
    options = menu.get_items()
    coffeeChoice = input(f"​What would you like? ({options})")
    if(coffeeChoice == "off"):
        isOn = False
    elif(coffeeChoice == "report"):
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(coffeeChoice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)