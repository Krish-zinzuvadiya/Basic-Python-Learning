# Recursion :- When a function calls itself repeatedly.

# prints n to 1 backwards
def show(n):  # Recursive Function
    if n == 0:
        return
    print(n)
    show(n-1)


show(5)


# Returns n!
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial Is : ", factorial(5))
