# Ex 1:- WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movie = []
movie.append(input("Enter Favorite Movie-1 : "))
movie.append(input("Enter Favorite Movie-2 : "))
movie.append(input("Enter Favorite Movie-3 : "))

print(movie)


# Ex 2:- WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("List is a palindrome")
else:
    print("List is not a palindrome")


# Ex 3:- WAP to count the number of students with the “A” grade in the following tuple.
grade = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
print(grade.count('A'))


# Ex 4:- Store the above values in a list & sort them from “A” to “D”
list2 = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
list2.sort()
print(list2)
