import turtle

t = turtle.Turtle()
t.speed(0)
t.color("#FF0000")
i = 1
while (True):
    for k in range(5):
        t.left(144)
        t.forward(200)
    t.left(10)
    i += 1
    if (i == 10):
        break


turtle.done()
turtle.exitonclick()
