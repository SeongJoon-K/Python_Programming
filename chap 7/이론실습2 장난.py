import turtle

t = turtle.Turtle("turtle")


def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font=('Times New Roman', 16, 'bold'))
