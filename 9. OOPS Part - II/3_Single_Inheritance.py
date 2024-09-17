# Inheritance : When one class(child/derived) derives the properties & methods of another class(parent/base).
# Example of Inheritance

# • Single Inheritance
class Car:
    color = "Black"

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")

print(car1.name)
print(car1.color)
print(car1.start())
print(car1.stop())
