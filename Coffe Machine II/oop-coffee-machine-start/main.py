from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

coffee_machine = CoffeeMaker()
money = MoneyMachine()
menu_coffee = Menu()

is_on = True

while is_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_choice == "report":
        print(coffee_machine.report())
        print(money.report())

    elif coffee_choice == "off":
        is_on = False

    else:
        beverage = menu_coffee.find_drink(coffee_choice)
        resource_valid = coffee_machine.is_resource_sufficient(beverage)
        money_valid = money.make_payment(beverage.cost)

        if resource_valid is True and money_valid is True:
            coffee_machine.make_coffee(beverage)
