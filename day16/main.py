from menu import (
    Menu,
    MenuItem,
)  # Menu Class: get_items(), find_drink(order_name) | MenuItem Class: name, cost, ingredients (all atributes)
from coffee_maker import (
    CoffeeMaker,
)  # CoffeeMaker Class: report(), is_resource_sufficient(drink), make_coffee(order)
from money_machine import (
    MoneyMachine,
)  # MoneyMachine Class: report(), make_payment(cost)

# from module import class

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    option = menu.get_items()
    choice = str(input(f"What would you like? {option}: "))
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):  # .cost is an atribute associated
                coffee_maker.make_coffee(drink)
