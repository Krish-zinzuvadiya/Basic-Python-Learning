# Ex 1:- Print the elements of the following list using a loop:
#        [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in list1:
    print(i)

print("End Of Loop")


# Ex 2:- Search for a number x in this tuple using loop:
#        [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
call1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49
idx = 0
for el in call1:
    if (el == x):
        print("Found At Index", idx)
        break
    idx += 1
