# Ex 1:- Average Of 3 numbers.
def avg(a, b, c):
    return (a + b + c) / 3


print("Average Is :", avg(10, 20, 30))


# Ex 2:- WAF to print the length of a list. ( list is the parameter)
cities = ["Delhi", "Gujrat", "Noida", "Mumbai", "Chennai"]


def print_len(list1):
    return len(list1)


print("Length of cities list is:", print_len(cities))


# Ex 3:- WAF to print the elements of a list in a single line. ( list is the parameter)
heroes = ["ironman", "thor", "shaktiman", "batman"]


def my_list(list2):
    for i in list2:
        print(i, end=" ")
    print()


my_list(heroes)


# Ex 4:- WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)


cal_fact(5)


# Ex 5:- WAF to convert USD to INR.
def convert_usd_to_inr(usd):
    inr = usd * 83
    print(usd, "USD =", inr, "INR")


convert_usd_to_inr(73)


# Ex 6(Bonus):- WAF To Print Number Is Odd or Even.
def num1():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


num1()
# Ex 7(Bonus):- WAF To Print The Largest Number In A List.

num1 = [2, 5, 3, 9, 6, 10]


def largest_num(list1):
    print("Largest Number Is : ", max(list1))


largest_num(num1)
