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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def money():
    quarters = float(input("How many quarters do you have? ($0.25): "))
    dimes = float(input("How many dimes do you have? ($0.10): "))
    nickels = float(input("How many nickels do you have? ($0.05): "))
    pennies = float(input("How many pennies do you have? ($0.01): "))

    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    print(total_money)
    return total_money


def report():
    report_result = ""
    report_result += str("coffee:" + str(resources["coffee"]) + "gr\n")
    report_result += str("milk:" + str(resources["milk"]) + "ml\n")
    report_result += str("water:" + str(resources["water"]) + "ml\n")
    report_result += str("profit: $") + str(profit)

    print(report_result)


drink = "on"
while True and drink != "off":
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "report":
        report()

    payment_processed = False
    for i in MENU:
        for a in MENU[i]["ingredients"]:
            if drink == i and resources[a] < MENU[i]["ingredients"][a]:
                print(f"There is not enough {a} in the machine")
                drink = "off"
                break

            elif drink == i and resources[a] >= MENU[i]["ingredients"][a] and not payment_processed:
                total_money_result = money()
                if total_money_result >= MENU[i]["cost"]:
                    resources[a] = resources[a] - MENU[i]["ingredients"][a]
                    print(resources)
                    total_money_result = round(total_money_result - MENU[i]["cost"], 2)
                    profit += MENU[i]["cost"]
                    print(f"Here is your change {total_money_result}. Enjoy your drink")
                    payment_processed = True

                else:
                    print("Sorry that's not enough money. Money refunded.")
                    drink = "off"
                    break
