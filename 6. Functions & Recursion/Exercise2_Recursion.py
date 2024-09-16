# Ex 1:- Write a recursive function to calculate the sum of first n natural numbers.
def rec(n):
    if n == 1:
        return 1
    else:
        return n + rec(n-1)


print(rec(5))
# Ex 2:- Write a recursive function to print all elements in a list. Hint : use list & index as parameters.
heroes = ["Hulk", "IronMan", "Caption America", "Thor", "Black Penther"]


def recursive_print(list1, index=0):
    if index == len(list1):
        return
    else:
        print(list1[index])
        recursive_print(list1, index+1)


recursive_print(heroes)
