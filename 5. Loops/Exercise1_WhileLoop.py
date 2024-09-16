# Ex 1:- Print Number from 1 to 100.
count = 1
while count <= 100:
    print(count)
    count += 1


# Ex 2:- Print numbers from 100 to 1.
count = 100
while count >= 1:
    print(count)
    count -= 1


# Ex 3:- Print the multiplication table of a number n.
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

# Ex 4:- Print the elements of the following list using loop.
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

index = 0
while index < len(num):
    print(num[index])
    index += 1


# Ex 5:- Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
call = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0

while i < len(call):
    if (call[i] == x):
        print("Found At Index", i)
        break
    else:
        print("Finding...")
    i += 1
