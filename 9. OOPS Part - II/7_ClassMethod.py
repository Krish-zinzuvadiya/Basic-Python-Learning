# Class Method : A class method is bound to the class & receives the class as an implict first argument.
# ---> Note : static method can't access or modify class state & generally for utility.
class Person:
    name = "null"

    @classmethod
    def change_name(cls, name):
        cls.name = name


p1 = Person()
p1.change_name("Rahul")
print(p1.name)
print(Person.name)
