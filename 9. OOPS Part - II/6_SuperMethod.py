# Super Method...
class Car:
    def __init__(self, type1):
        self.type1 = type1

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  # Super Constructor...


car1 = ToyotaCar("Prius", "Electric")
print(car1.type1)
