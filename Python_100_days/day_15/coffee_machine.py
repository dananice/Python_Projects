# TODO print report
# TODO check if resources are sufficient
# TODO Process coins
# TODO Prompt user "What would you like? (espresso/
# latte/cappuccino):"
# TODO Turn off the Coffee Machine by entering "off"
# TODO CHECK if transaction successful
# TODO Make coffee & reduce resources

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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# check if resources are sufficient for drink request
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True    
            
# Process coins
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dime?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
    
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficent."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money.  Money refunded.")
        return False
 
def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")    
    
       
is_on = True

while is_on:
    
    user_request = input("What would you like? (espresso/latte/cappuccino): ")
    if user_request == "off":
        is_on = False
    elif user_request == 'report':   
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}" )
    else:
        drink = MENU[user_request] 
        if check_resources(drink["ingredients"]): 
            payment = process_coins() 
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_request, drink["ingredients"])
            
        




        
              
        
 
    
