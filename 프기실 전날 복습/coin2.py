import random
import turtle

t = turtle.Turtle("turtle")

screen = turtle.Screen()
image1 = "front.GIF"
image2 = "back.GIF"
screen.addshape(image1)
screen.addshape(image2)

coin = random.randint(0, 1)

if coin == 1:
    t.shape(image1)
    t.stamp()
else:
    t.shape(image2)
    t.stamp()


turtle.done()
turtle.exitonclick()
