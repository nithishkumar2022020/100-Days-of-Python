
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid = {}
def auction(name,amt):
    bid[name] = amt

def highest_bid():
    high=0
    winner=""
    for name, amt in bid.items():
        if amt > high:
            high = amt
            winner = name
    print(f"the winner is {winner} with {high}")


def inp():

    name = input("What is your name? ")
    amt = int(input("Enter your bid "))
    auction(name,amt)
print("Welcome to the secret auction program.")


while True:
    name = input("What is your name? ")
    amt = int(input("Enter your bid: "))
    auction(name, amt)

    nextt = input("Is there another bidder? Type 'yes' or 'no': ").lower()

    if nextt == 'no':
        highest_bid()
        break
    elif nextt == 'yes':
        continue
    else:
        print("Enter a Valid Input")
        nextt = input("Is there another bidder? Type 'yes' or 'no': ").lower()

