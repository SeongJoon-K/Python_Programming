class Car:
    def drive(self):  # 클래스 메소드의 첫 번째 매개변수는 항상 self로 현개 객체를 가르킨다

        self.speed = 10


myCar = Car()

myCar.color = "blue"
myCar.model = "이클래스"
myCar.speed = 0
myCar.year = "2017"

myCar.drive()
print(myCar.speed)
