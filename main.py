machine_on = True

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
            "water": 200
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
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_supplies():
    for res in resources:
        print(f"{res}:  {resources[res]}")


def make_coffee(coffee_type):
    # deduct coffee needs from supplies
    water = (MENU[coffee_type]["ingredients"]["water"])
    coffee = (MENU[coffee_type]["ingredients"]["coffee"])
    cost = (MENU[coffee_type]["cost"])
    if coffee_type != "espresso":
        milk = (MENU[coffee_type]["ingredients"]["milk"])
    else:
        milk = 0

    print(f"you need water:{water}  coffee:{coffee}  milk:{milk} for {coffee_type}")

    if water < resources['water'] and milk < resources['milk'] and coffee < resources['coffee']:
        print(f"Adequate Resouces!!!!!: Now Making your {coffee_type}")
        payment = float(input(f"Please deposit {cost} to make your coffee!"))
        if payment == cost:
            resources['water'] -= water
            resources['milk'] -= milk
            resources['coffee'] -= coffee
            total_money += payment
            print("Here is your coffee!!!!!")
        elif payment > cost:
            refund = payment - cost
            total_money += payment
            print(f"Your refund is {refund}")


    else:
        print("Machine needs to be refilled")

while machine_on:
    user_choice = input("What would you like? 1. Espresso, "
                        "2. Latte, 3. Cappuccino: ")

    if user_choice == "1":
        check_supplies()
        make_coffee("espresso")
    if user_choice == "2":
        check_supplies()
        make_coffee("latte")
    if user_choice == "3":
        check_supplies()
        make_coffee("cappuccino")

    if user_choice.lower() == 'off':
        machine_on = False
