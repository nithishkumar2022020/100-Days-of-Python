def espresso(w_esp, mi_esp, c_esp, mo_esp):
    """Handle the preparation of an espresso."""

    req_water = 50
    req_milk = 0
    req_coffee = 18
    cost = 1.5


    if w_esp < req_water:
        print("Sorry, there is not enough water.")
        inp(w_esp, mi_esp, c_esp, mo_esp)
    elif c_esp < req_coffee:
        print("Sorry, there is not enough coffee.")
        inp(w_esp, mi_esp, c_esp, mo_esp)
    else:

        print("Please insert coins.")
        total = insert_coins()
        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.") if change > 0 else None
            print("Here is your espresso. Enjoy!")

            w_esp -= req_water
            c_esp -= req_coffee
            mo_esp += cost
        else:
            print("Sorry, that's not enough money. Money refunded.")
    inp(w_esp, mi_esp, c_esp, mo_esp)


def latte(w_lat, mi_lat, c_lat, mo_lat):
    """Handle the preparation of a latte."""
    req_water = 200
    req_milk = 150
    req_coffee = 24
    cost = 2.5

    if w_lat < req_water:
        print("Sorry, there is not enough water.")
        inp(w_lat, mi_lat, c_lat, mo_lat)
    elif mi_lat < req_milk:
        print("Sorry, there is not enough milk.")
        inp(w_lat, mi_lat, c_lat, mo_lat)
    elif c_lat < req_coffee:
        print("Sorry, there is not enough coffee.")
        inp(w_lat, mi_lat, c_lat, mo_lat)
    else:
        print("Please insert coins.")
        total = insert_coins()
        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.") if change > 0 else None
            print("Here is your latte. Enjoy!")
            w_lat -= req_water
            mi_lat -= req_milk
            c_lat -= req_coffee
            mo_lat += cost
        else:
            print("Sorry, that's not enough money. Money refunded.")
    inp(w_lat, mi_lat, c_lat, mo_lat)


def cappuccino(w_cap, mi_cap, c_cap, mo_cap):
    """Handle the preparation of a cappuccino."""
    req_water = 250
    req_milk = 100
    req_coffee = 24
    cost = 3.0

    if w_cap < req_water:
        print("Sorry, there is not enough water.")
        inp(w_cap, mi_cap, c_cap, mo_cap)
    elif mi_cap < req_milk:
        print("Sorry, there is not enough milk.")
        inp(w_cap, mi_cap, c_cap, mo_cap)
    elif c_cap < req_coffee:
        print("Sorry, there is not enough coffee.")
        inp(w_cap, mi_cap, c_cap, mo_cap)
    else:
        print("Please insert coins.")
        total = insert_coins()
        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.") if change > 0 else None
            print("Here is your cappuccino. Enjoy!")
            w_cap -= req_water
            mi_cap -= req_milk
            c_cap -= req_coffee
            mo_cap += cost
        else:
            print("Sorry, that's not enough money. Money refunded.")
    inp(w_cap, mi_cap, c_cap, mo_cap)


def insert_coins():
    """Ask the user to insert coins and calculate the total."""
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return round(quarters + dimes + nickels + pennies, 2)


def inp(w, mi, c, mo):
    """Handle user input and control the coffee machine."""
    ip = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ip == 'espresso':
        espresso(w, mi, c, mo)
    elif ip == 'latte':
        latte(w, mi, c, mo)
    elif ip == 'cappuccino':
        cappuccino(w, mi, c, mo)
    elif ip == 'report':
        print(f"The current resources are:\nWater: {w}ml\nMilk: {mi}ml\nCoffee: {c}g\nMoney: ${mo}")
        inp(w, mi, c, mo)
    elif ip == 'off':
        print("Turning off the coffee machine. Goodbye!")
        exit()
    else:
        print("Enter a valid input.")
        inp(w, mi, c, mo)


# Initial resources
Water = 300
Milk = 200
Coffee = 100
Money = 0.0

inp(Water, Milk, Coffee, Money)
