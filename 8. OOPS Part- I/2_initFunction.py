# __init__ Function
# ---> Constructor : All classes have a function called __init__(), which is always executed when the object is being initiated.

# Self Parameter : The self parameter is a reference to the current
#                  instance of the class , and is used to access variables
#                  that belongs to the class .


class Student1:
    name = "Karan"  # • Class Attribute

    # ⌂ Default Constructor
    def __init__(self):
        print("adding new student in database...")


s1 = Student1()
print(s1.name)

# Self & fullname combination...


class Student2:
    # ⌂ Parameterized Constructor
    def __init__(self, fullname):
        self.name = fullname  # • Object(Instance) Attribute
        print("adding new student in database...")


s2 = Student2("Krish")
print(s2.name)

s3 = Student2("Arjun")
print(s3.name)
