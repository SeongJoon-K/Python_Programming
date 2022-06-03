from turtle import *  # 터틀을 임포트 한다


class Car:  # Car class를 import 한다
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car.gif")
# 생성자를 사용해 속도, 컬러, 모델명을 입력받는다. self는 가장 처음 들어가는 매개변수다.

    def drive(self):  # 입력된 값만큼, 앞으로 간다
        self.turtle.fd(self.speed)

    def left_turn(self):  # 입력된 수만큼 왼쪽으로 돈다
        self.turtle.left(90)


register_shape("car.gif")  # 모양을 설정한다
myCar = Car(200, "red", "E-class")  # Car클래스를 myCar로 설정하고 생성자를 대입한다
for i in range(100):  # for문을 100번 돌린다
    myCar.drive()  # drive 함수를 사용하고, 생성자에 입력된 200만큼 대입한다.
    myCar.left_turn()  # 기존 함수정의 생성자에 입력된 왼쪽으로 90도 꺾는다.

done()  # 함수를 종료시킨다.
exitonclick()
