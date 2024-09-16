# Ex 1:- Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)
    i += 1


# Ex 2:- Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)


# Ex 3:- Print the multiplication table of a number n.
n = int(input("Enter Number:- "))
for i in range(1, 11):
    print(n*i)
