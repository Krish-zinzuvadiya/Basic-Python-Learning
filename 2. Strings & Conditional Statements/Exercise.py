# Ex 1:- WAP to input user’s first name & print its length.
print("-------------------------------------------")
print("Exercise 1 :")
name = input("Enter Your First Name :- ")
print("Length Of Your Name Is : ", len(name))
print("-------------------------------------------")

# Ex 2:- WAP to find the occurrence of ‘$’ in a String.
print("Exercise 2 :")
example = "Hi, $ I Am The $ Symbol $ 19.36"
print("The $ symbol occurs ", example.count('$'), " times in the string.")
print("-------------------------------------------")


# Ex 3:- WAP to check if a number entered by the user is odd or even.
print("Exercise 3 :")
num = int(input("Enter Number : "))
if (num % 2 == 0):
    print("Number Is Even")
else:
    print("Number Is Odd")
print("-------------------------------------------")


# Ex 4:- WAP to find the greatest of 3 numbers entered by the user.
print("Exercise 4 :")
num1 = int(input("Enter Number-1 : "))
num2 = int(input("Enter Number-2 : "))
num3 = int(input("Enter Number-3 : "))
if (num1 >= num2 and num1 >= num3):
    print("Greatest Number Is : ", num1)
elif (num2 >= num3):
    print("Greatest Number Is : ", num2)
else:
    print("Greatest Number Is : ", num3)
print("-------------------------------------------")


# Ex 5:- WAP to check if a number is a multiple of 7 or not.
print("Exercise 5 :")
i = int(input("Enter Number : "))
if (i % 7 == 0):
    print(i, " is a multiple of 7")
else:
    print(i, " is not a multiple of 7")
print("-------------------------------------------")
