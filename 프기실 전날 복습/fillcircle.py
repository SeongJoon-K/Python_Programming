import turtle

t = turtle.Turtle("turtle")

color_list = ["yellow", "red", "blue", "green"]

for i in range(0, 4):
    t.fillcolor(color_list[i])  # 채우기 색상 설정
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.fd(50)


turtle.done()
turtle.exitonclick()
