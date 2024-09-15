# Lists :- A built-in data type that stores set of values

marks = [94.4, 87.5, 95.2, 66, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

# It can store elements of different types (integer, float, string, etc.)
student = ["smit", 98.4, "Gujrat"]
print(student)
student[0] = "krish"
print(student)

# 🌟 Strings Are Immutable In Python. (things cannot change)
# 🌟 Lists Are Mutable In Python. (things can change)

# Lists Slicing
marks1 = [65, 35, 45, 88, 98]
print(marks1[1:4])  # also include negative index..
print(marks1[1:])  # from index 1 to the end
print(marks1[:4])  # from the start to index 4
print(marks1[:])  # from the start to the end
print(marks1[-1])  # last element
