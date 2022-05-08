import turtle

t = turtle.Turtle("turtle")

a = int(input("몇 각형을 그릴건가요?"))
b = int(input("몇 번 그릴건가요?"))

# n 각형 그리는 함수


def n_polygon(num, dist):
    for i in range(a):
        t.left(360/num)
        t.fd(dist)


for i in range(b):
    t.left(20)
    n_polygon(a, 100)

turtle.done()
turtle.exitonclick()
