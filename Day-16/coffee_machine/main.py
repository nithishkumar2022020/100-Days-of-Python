from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


isOn=True
while isOn:
    options = menu.get_items()
    choice = input(f"what would you like to have {options}")
    if choice == "off":
        isOn=False
    elif choice == 'on' and choice == 'report':
        print(money_machine.report())
        print(coffee_maker.report())
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)