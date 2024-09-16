# Abstraction : Abstraction is hiding internal details and showing only essential features of an object.
# Encapsulation : Encapsulation is bundling data and methods that operate on that data within a single unit.
# Inheritance :  Inheritance is a mechanism where a new class inherits properties and behavior of an existing class.
# Polymorphism : Polymorphism is the ability of an object to take on multiple forms.


# Here Important...

# Abstraction :- Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False

    def start(self):
        self.cluth = True
        self.acc = True
        print("Car Started...")


car1 = Car()
car1.start()

# Encapsulation :- Wrapping data and functions into a single unit (object).
