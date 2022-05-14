import turtle
import random

t = turtle.Turtle("turtle")
x = 0
y = 0
color_list = ["yellow", "red", "blue"]
c = ""


def draw_square(x, y, c):
    x = random.randrange(-100, 101)
    y = random.randrange(-100, 101)
    for i in ["yellow", "red", "blue"]:
        c = random.choice(color_list)


for i in range(4):
    draw_square(x, y, c)
    t.goto(x, y)
    t.fillcolor(c)
    t.begin_fill()
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.end_fill()

turtle.done()
turtle.exitonclick()
