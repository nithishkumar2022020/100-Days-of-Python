from turtle import *
import time
import random

# Screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake setup
pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for i in pos:
    turtle = Turtle()
    turtle.shape("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(i)
    segments.append(turtle)

# Food setup
food = Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Score setup
score = 0
scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.color("white")
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Movement variables
game_on = True
direction = "right"
next_direction = "right"

def move_up():
    global next_direction
    if direction != "down":
        next_direction = "up"

def move_down():
    global next_direction
    if direction != "up":
        next_direction = "down"

def move_left():
    global next_direction
    if direction != "right":
        next_direction = "left"

def move_right():
    global next_direction
    if direction != "left":
        next_direction = "right"

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
while game_on:
    screen.update()
    time.sleep(0.1)

    # Update snake's direction
    direction = next_direction  # Removed the incorrect 'global' declaration

    # Move snake body
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    # Move head of the snake
    if direction == "up":
        segments[0].setheading(90)
    elif direction == "down":
        segments[0].setheading(270)
    elif direction == "left":
        segments[0].setheading(180)
    elif direction == "right":
        segments[0].setheading(0)
    segments[0].forward(20)

    # Check for collision with food
    if segments[0].distance(food) < 15:
        score += 1
        scoreboard.clear()
        scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Add a new segment to the snake
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

    # Check for collision with walls
    if (
        segments[0].xcor() > 280
        or segments[0].xcor() < -280
        or segments[0].ycor() > 280
        or segments[0].ycor() < -280
    ):
        game_on = False

    # Check for collision with itself
    for segment in segments[1:]:
        if segments[0].distance(segment) < 10:
            game_on = False

# Game over screen
game_over = Turtle()
game_over.hideturtle()
game_over.penup()
game_over.color("white")
game_over.goto(0, 0)
game_over.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

screen.exitonclick()
