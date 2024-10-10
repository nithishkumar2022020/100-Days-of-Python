rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

num=random.randint(1,3)
unum=input("Rock, paper, scissors? enter 1,2 or 3")
print("computer choice is: \n")
if num==1:

    print(rock)
elif num==2:
    print(paper)
else:
    print(scissors)
print("your choice is: \n")
if unum == 1:

    print(rock)
elif unum == 2:
    print(paper)
else:
    print(scissors)
if num==unum:
    print("Draw")
elif unum==1 and num==3:
    print("You Win")
elif unum==2 and num==1:
    print("You Win")
elif unum==3 and num==2:
    print("You Win")
else:
    print("You Lose")