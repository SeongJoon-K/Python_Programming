class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60


myCar = Car(0, "blue", "e클래스")
dadCar = Car(0, "sice", "A6")
momCar = Car(0, "white", "520d")

momCar.drive()
print(dadCar.model)

# self의 역할은 어떤 객체가 메소드를 호출했는지 알려주는 역할이다
