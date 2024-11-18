import random
def chance():
    if input("Easy or Hard").lower()=="easy":
        ch=10

    else:
        ch=5
    return ch

def rangee(b,a):
    if b>a:
        print("Too big")
    elif b<a:
        print("Too small")


def guess():
    a1=random.randint(1,100)
    cha=0
    num=chance()

    while cha<=num:
        b1=int(input("Guess a number between 1 and 100"))
        if a1==b1:
            print(f"You guessed correctly!, the number is {a}")
            break
        else:
            rangee(b1,a1)
            cha += 1
            print(f"you have {num-cha} attempts remaining")
            if num-cha==0:
                break

#
#
guess()

if input("do you want to try again? y/n").lower()=="y":
    guess()
else:
    print("Thank you for playing")