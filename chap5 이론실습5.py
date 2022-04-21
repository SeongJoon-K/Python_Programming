import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하세요")
w = turtle.textinput("", "가로 길이를 입력하세요")
h = turtle.textinput("", "세로 길이를 입력하세요")

if s == "사각형":
    t.forward(int(w))
    t.left(90)
    t.forward(int(h))
    t.left(90)
    t.forward(int(w))
    t.left(90)
    t.forward(int(h))

turtle.done()
