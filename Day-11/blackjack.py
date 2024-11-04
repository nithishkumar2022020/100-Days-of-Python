
# ask if user wants to play the game or not
#
# create list for comp and user
#
# fn to add all elements in list
#
# ask for n until the user wins/looses
# if tot >= 21 along with a, then a =1
# else a=1
#
# whoever reaches 21 first, looses

import random

def blackjack():
    # Draw a card for the player
    p1.append(random.choice(num))
    ps1 = sum1(p1)
    print(f"Your deck is {p1}, total = {ps1}")

    # Draw a card for the computer
    a1.append(random.choice(num))
    as1 = sum1(a1)
    print(f"Computer's deck is {a1}, total = {as1}")

    return ps1, as1


def sum1(s1):
    res = 0
    for x in s1:
        res += x
    return res


# Initialize variables
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
p1 = []
a1 = []

# Ask if the user wants to play
play = input("Would you like to play a game of blackjack? ('y/n'): ")
if play.lower() == 'y':
    while True:
        # Draw a card for both player and computer
        ps1, as1 = blackjack()

        # Check if player or computer has reached or exceeded 21
        if ps1 >= 21:
            print("You reached 21 or more! You lose!")
            break
        elif as1 >= 21:
            print("Computer reached 21 or more! You win!")
            break

        # Ask player if they want to continue
        cont = input("Do you want to draw another card? ('y/n'): ")
        if cont.lower() != 'y':
            print("You chose to hold.")
            break

    # Final scores
    print(f"Final player deck: {p1}, total = {sum1(p1)}")
    print(f"Final computer deck: {a1}, total = {sum1(a1)}")
else:
    print("Maybe next time!")