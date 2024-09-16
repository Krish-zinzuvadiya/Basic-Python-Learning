# Non-Static Methods : Methods are functions that belong to objects.
class Student:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome to the Python world!", self.name)


s = Student("Karan")
s.welcome()


# Static Methods :Methods that don’t use the self parameter (work at class level)

# Use Of Decorator :- Decorators allow us to wrap another function in order to
#                     extend the behaviour of the wrapped function, without
#                     permanently modifying it
class Student1():
    @staticmethod  # --> Decorator
    def colleeg():
        print("Lj College")


s1 = Student1()
Student1.colleeg()
