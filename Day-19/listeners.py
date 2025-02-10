from turtle import *
tim=Turtle()
screen=Screen()

def move_forwards():
    tim.forward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)
    
def move_back():
    tim.backward(10)

def clear():
    tim.clearscreen()
    tim.home()
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="x",fun=clear)
screen.exitonclick()
