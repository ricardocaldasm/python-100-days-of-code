MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sufficient_resource(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False    
    return True

def process_coins(drink):
    print(f"The {drink} costs ${MENU[drink]["cost"]}. Please insert coins.")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.1
    nickles = float(input("How many nickles? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name}!")

profit = 0

while True:
    choice = str(
        input("What would you like? (espresso/latte/cappuccino) or (report/off): ")
    )
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}m\nCoffee: {resources['coffee']}ml\nProfit: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if sufficient_resource(drink["ingredients"]):
            payment = process_coins(choice)
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

    else:
        print("Invalid input.")

