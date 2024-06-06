from machine_data import MENU, resources

profit = 0


# TODO 3: Print a report of all the coffee machine resources
def status_report():
    """Gives a status report of the quantity of resources left"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# TODO 4: Check resources sufficient to make drink order
def resource_insufficient(choice):
    """Checks to confirm there are enough resources to make the order"""
    ingredients = choice["ingredients"]
    for i in ingredients:
        if ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i} for this order.")
            return True


# TODO 7: Make the coffee order
def process_order(choice):
    ingredients = choice["ingredients"]
    for i in ingredients:
        resources[i] -= ingredients[i]


# TODO 5: Process coin payment for drink order

def order_payment(choice, menu_item):
    """Accepts user payment and processes order. Also updates the quantity of resources."""
    print("Please insert some coins.")
    total_paid = int(input("How many quarters? ")) * 0.25
    total_paid += int(input("How many dimes? ")) * 0.10
    total_paid += int(input("How many nickles? ")) * 0.05
    total_paid += int(input("How many pennies? ")) * 0.01

    price = choice["cost"]
    # TODO 6: Check if the drink order transaction successful
    if total_paid < price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        process_order(choice)
        if total_paid > price:
            customer_change = round(total_paid - price, 2)
            print(f"You get ${customer_change} in change.")
        print(f"Here is your {menu_item} ☕ Enjoy!")


def menu_option(item):
    global profit
    """Select the coffee machine menu item based on the user's choice"""
    if item == "report":
        status_report()
    else:
        drink = MENU[item]
        if not resource_insufficient(drink):
            order_payment(drink, item)
            profit += drink["cost"]


# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
machine_on = True

while machine_on:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        machine_on = False
    else:
        menu_option(order)
