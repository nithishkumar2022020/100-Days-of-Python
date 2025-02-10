from random import randint
from turtle import Turtle, Screen


colors = ["blue", "green", "yellow", "orange", "grey", "purple"]


screen = Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput("Place your Bet", "Who will win? Enter a color:")


y_positions = [-150, -100, -50, 0, 50, 100]


all_turtles = []


for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])
    all_turtles.append(tim)


if user_bet:
    race_on = True
else:
    race_on = False


while race_on:
    for turtle in all_turtles:
        # Move the turtle forward by a random distance
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

        # Check if the turtle has crossed the finish line
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break  # Exit the loop once a winner is found


screen.exitonclick()
