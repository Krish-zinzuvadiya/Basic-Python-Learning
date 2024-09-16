# Functions :- Block of statements that perform a specific task.

# Function Definations
def sum1(a, b):  # Parameters
    return a+b


print("Sum Is :", sum1(5, 10))  # Function Call; Arguments


# Functions Type :
# --> 1. Built-in Functions
print("Krish")
str1 = "Python"  # i. print()
st = len(str1)  # ii. len()
print("Length Of String Is :", st)
a1 = type(str1)  # iii. type()
print(a1)

for i in range(1, 6):  # iv. range()
    print(i)

# --> 2. User defined Functions :-


def calc_prod(a, b):
    print(a*b)
    return a*b


calc_prod(3, 2)
