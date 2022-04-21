import turtle
t = turtle.Turtle()
t.shape("turtle")
x1 = int(input("큰 원의 시작좌표 x1: "))
y1 = int(input("큰 원의 시작좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 시작좌표 x2: "))
y2 = int(input("작은 원의 시작좌표 y2: "))
r2 = int(input("작은 원의 작은원: "))

t.pendown()
t.goto(x1, y1)
t.circle(r1)
t.penup()

t.goto(x2, y2)
t.pendown()
t.circle(r2)
t.penup()
dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
if r1 > dist and r1 > r2:
    turtle.write("두 번째 원이 첫 번째 원의 내부에 있습니다.")
elif r1 == r2 and dist == 0:
    turtle.write("두 번째 원이 첫 번째 원과 겹칩니다.")
else:
    turtle.write("두 번째 원이 첫 번째 원과 겹치지 않습니다.")
turtle.done()
