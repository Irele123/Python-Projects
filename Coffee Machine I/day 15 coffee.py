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

money_value= {
    "quarters":0.25,
    "dimes":0.10, 
    "nickels":0.05,
    "pennies":0.01
    }

report="report"

resources["money"]=0

bev_choice=input("What would you like? (espresso/latte/cappuccino):")

print("Please insert coins")

quarters=int(input("How many quarters?"))
dimes=int(input("How many dimes?"))
nickels=int(input("How many nickels?"))
pennies=int(input("How many pennies?"))

money_inserted=(quarters*money_value["quarters"])+(dimes*money_value["dimes"])+(nickels*money_value["nickels"])+(pennies*money_value["pennies"])
change=0

valid_milk=False
valid_water=False
valid_coffee=False
valid_change=False

if bev_choice == report:
    print("Water: "+str(resources["water"]))
    print("Milk: "+str(resources["milk"]))
    print("Coffee: "+str(resources["coffee"]))
    print("Money: "+str(resources["money"]))

elif bev_choice=="espresso":
    resources["milk"]=resources["milk"]-MENU["espresso"]["ingredients"]["milk"]
    resources["coffee"]=resources["coffee"]-MENU["espresso"]["ingredients"]["coffee"]
    resources["water"]=resources["water"]-MENU["espresso="]["ingredients"]["water"]
    change=money_inserted-MENU["espresso"]["cost"]
        
    resources["money"]=resources["money"]+MENU["espresso"]["cost"]

elif bev_choice=="latte":
    resources["milk"]=resources["milk"]-MENU["latte"]["ingredients"]["milk"]
    resources["coffee"]=resources["coffee"]-MENU["latte"]["ingredients"]["coffee"]
    resources["water"]=resources["water"]-MENU["latte"]["ingredients"]["water"]
    change=money_inserted-MENU["latte"]["cost"]
    
    resources["money"]=resources["money"]+MENU["latte"]["cost"]

elif bev_choice=="cappuccino":
    resources["milk"]=resources["milk"]-MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"]=resources["coffee"]-MENU["cappuccino"]["ingredients"]["coffee"]
    resources["water"]=resources["water"]-MENU["cappuccino"]["ingredients"]["water"]
    change=money_inserted-MENU["cappuccino"]["cost"]
    
    resources["money"]=resources["money"]+MENU["cappuccino"]["cost"]


if change < 0:
    print("Sorry that's not enough money. Money refunded.")

else:
    if change > 0:
        change=round(change,2)
        print(f"Here is {change} in change.")
    
    else:
        print("No change.")
    

    if (resources["milk"] < 0):
        print("Sorry there is not enough milk")

    elif (resources["coffee"] < 0):
        print("Sorry there is not enough coffee")
    
    elif (resources["water"] < 0):
        print("Sorry there is not enough water")
    

    else:
        print(f"Here is your {bev_choice}. Enjoy!")

#USE MORE FUNCTIONS FROM DAY 16