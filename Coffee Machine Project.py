from xxsubtype import bench

menu= {
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

money= 0

def calc_money(coffee, money_required, nq, nd, nn, np,earning):
    input_money= (nq*0.25) + (nd*0.10) + (nn*0.05) + (np*0.01)
    change =  input_money-money_required
    if change==0:
        earning+=money_required
        print(f"Here is your {coffee}☕ Enjoy!")
        return earning
    elif change>0:
        earning += money_required
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee}☕ Enjoy!")
        return earning
    elif change<0:
        print(f"Not enough money . Here is your given amount of ${input_money}")
        return None
    return None


def coffee_making(user_input,money):
    updated_money=money
    if user_input == "report":
        print(f"Water  : {resources["water"]}ml")
        print(f"Milk   : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}grams")
        print(f"Money  : ${money}")
        return money
    else:
        if menu[user_input]["ingredients"]["water"] <= resources["water"] and menu[user_input]["ingredients"][
            "coffee"] <= resources["coffee"]:
            n_quarters = int(input("How many quarters? : "))
            n_dimes = int(input("How many dimes? : "))
            n_nickels = int(input("How many nickels? : "))
            n_pennies = int(input("How many pennies? : "))
            updated_money= calc_money(user_input, menu[user_input]["cost"], n_quarters, n_dimes, n_nickels, n_pennies, money)
            if updated_money != 0:
                resources["water"] -= menu[user_input]["ingredients"]["water"]
                resources["coffee"] -= menu[user_input]["ingredients"]["coffee"]
        else:
            if menu[user_input]["ingredients"]["water"] > resources["water"]:
                print("Sorry. There is not enough water!")
            elif menu[user_input]["ingredients"]["coffee"] >= resources["coffee"]:
                print("Sorry. There is not enough coffee!")
            else:
                print("Sorry. There is not enough milk!")
        return updated_money


while 1<5:
    user_input = input("What would you like ? (espresso/latte/cappuccino): ").lower()
    if user_input!= "report" and user_input!= "espresso" and user_input!= "latte" and user_input!= "cappuccino":
        print("Invalid Input. Try Again!")
    else:
        money=coffee_making(user_input,money)
