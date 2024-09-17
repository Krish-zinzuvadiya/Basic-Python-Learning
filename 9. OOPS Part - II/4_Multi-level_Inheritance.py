# • Multi-level Inheritance
class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type1):
        self.type = type1


car1 = Fortuner("Diesel")
car1.start()
