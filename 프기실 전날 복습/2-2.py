# 도전문제 2장 이론실습 3

# name = input("이름을 입력하세요 : ")
# print(name, "씨, 안녕하세요>")
# print("파이썬에 오신 것을 환영합니다.")

# x = int(input("첫 번째 정수를 입력하시오 : "))
# y = int(input("두 번째 정수를 입력하시오 : "))
# sum = x+y
# print(x, "과", y, "의 합은", sum, "입니다")

# Lap 집 그리기

import turtle

t = turtle.Turtle("turtle")
radius = int(input("집 크기 얼마로 할까"))
t.forward(radius)
t.left(90)
t.forward(radius)
t.left(90)
t.forward(radius)
t.left(90)
t.forward(radius)
t.left(90)

t.forward(radius)
t.left(90)
t.forward(radius)
t.left(30)
t.forward(radius)
t.left(120)
t.forward(radius)
t.left(120)

turtle.done()
turtle.exitonclick()
