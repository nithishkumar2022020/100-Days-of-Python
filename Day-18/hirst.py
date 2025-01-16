import turtle as t_m
import random
t= t_m.Turtle()

screen=t_m.Screen()
screen.colormode(255)
colors = [ (244, 123, 30), 
           (122, 202, 21),
           (135, 206, 250),
           (255, 20, 147),
           (75, 0, 130),
           (255, 215, 0),
           (0, 255, 127),
           (123, 104, 238),
           (200, 128, 128)]
t.pencolor("white")
t.penup()
t.ht()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
dots=100

for i in range(1,dots+1):
    screen.colormode(255)
    t.dot(20,random.choice(colors))
    t.forward(50)

    if i%10==0:
        screen.colormode(255)
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
