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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


resources["money"] = 0


def coffee_machine():

    def order():
        print("Please insert coins.")
        quarters = float(input("how many quarters?: "))
        dimes = float(input("how many dimes?: "))
        nickles = float(input("how many nickles?: "))
        pennies = float(input("how many pennies?: "))
        sum_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        return sum_coins

    def check_money(money_inserted):
        if money_inserted >= MENU[request]["cost"]:
            return True
        else:
            False

    def check_resources(request):
        if request == "latte" or request == "cappuccino":
            if resources["water"] - MENU[request]["ingredients"]["water"] >= 0:
                if resources["milk"] - MENU[request]["ingredients"]["milk"] >= 0:
                    if resources["coffee"] - MENU[request]["ingredients"]["coffee"] >= 0:
                        return True
                    else:
                        print("Sorry we don't have coffee any more")
                        return False
                else:
                    print("Sorry we don't have milk any more")
                    return False
            else:
                print("Sorry we don't have water any more")
                return False
        elif request == "espresso":
            if resources["water"] - MENU[request]["ingredients"]["water"] >= 0:
                if resources["coffee"] - MENU[request]["ingredients"]["coffee"] >= 0:
                    return True
                else:
                    print("Sorry we don't have coffee any more")
                    return False
            else:
                print("Sorry we don't have water any more")
                return False

    def serve(money_inserted):
        if money_inserted - MENU[request]["cost"] < 0:
            return"Sorry that's not enough money. Money refunded."
        elif money_inserted - MENU[request]["cost"] == 0:
            print("Here is $0.0 in change.")
            print(f"Here is your {request}. Enjoy!")
        elif money_inserted - MENU[request]["cost"] > 0:
            change = money_inserted - MENU[request]["cost"]
            change = round(change, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {request}. Enjoy!")

    def reduce_resources(request):
        if request == "latte" or request == "cappuccino":
            resources["water"] -= MENU[request]["ingredients"]["water"]
            resources["milk"] -= MENU[request]["ingredients"]["milk"]
            resources["coffee"] -= MENU[request]["ingredients"]["coffee"]

        elif request == "espresso":
            resources["water"] -= MENU[request]["ingredients"]["water"]
            resources["coffee"] -= MENU[request]["ingredients"]["coffee"]
        resources["money"] += MENU[request]["cost"]
        return resources

    def report(resources):
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        money = resources["money"]
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

    # TODO 1: add MONEY to the dictionary resources

    # TODO 2: ask the client their choice

    request = True
    while request:
        request = input("  What would you like? (espresso/latte/cappuccino): ")
        if request == "off":
            request = False
        if request == "espresso":
            is_enough_resources = check_resources(request)
            if is_enough_resources:
                money_inserted = order()
                is_enough = check_money(money_inserted)
                if is_enough:
                    serve(money_inserted)
                    reduce_resources(request)
                elif not is_enough:
                    print("Sorry not enough money. Money refunded.")
        elif request == "latte":
            is_enough_resources = check_resources(request)
            if is_enough_resources:
                money_inserted = order()
                is_enough = check_money(money_inserted)
                if is_enough:
                    serve(money_inserted)
                    reduce_resources(request)
                elif not is_enough:
                    print("Sorry not enough money. Money refunded.")
        elif request == "cappuccino":
            is_enough_resources = check_resources(request)
            if is_enough_resources:
                money_inserted = order()
                is_enough = check_money(money_inserted)
                if is_enough:
                    serve(money_inserted)
                    reduce_resources(request)
                elif not is_enough:
                    print("Sorry not enough money. Money refunded.")
        if request == "report":
            report(resources)
            coffee_machine()




coffee_machine()
