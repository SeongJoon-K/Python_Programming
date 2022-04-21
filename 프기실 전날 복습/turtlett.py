import turtle

t = turtle.Turtle()
t.shape('turtle')

while True:
    move = input()

    if(move == "l"):
        t.left(90)
        t.fd(100)
    elif move == "r":
        t.right(90)
        t.fd(100)
    else:
        break

turtle.done()
turtle.exitonclick()
