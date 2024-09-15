# Lists Method
list1 = [2, 1, 3]

# adds one element at the end
list1.append(4)  # mutating the list
print(list1)

# sorts in ascending order
list1.sort()
print("Sorted List in Ascending Order: ", list1)

list1.sort(reverse=True)
print("Sorted List in Descending Order : ", list1)

# reverses list
list1.reverse()
print("Reversed List: ", list1)

# insert element at index
list1.insert(2, 5)
print(list1)

# removes first occurrence of element
list1.remove(1)
print(list1)

# removes element at index
list1.pop(0)
print(list1)
