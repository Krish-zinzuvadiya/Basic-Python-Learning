# Ex 1:- Store following word meanings in a python dictionary
# table : “a piece of furniture” , “list of facts & figures”
# cat : “a small animal”

cat_dict = {
    "cat": "a small animal",
}
print(cat_dict)

table_dict = {
    "table": ["a piece of furniture", "list of facts & figures"]
}
print(table_dict)


# Ex 2:- You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}
print(len(subjects))


# Ex 3:- WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
marks = {}
m1 = int(input("Enter Physics Marks : "))
marks.update({"phy": m1})

m2 = int(input("Enter Maths Marks : "))
marks.update({"maths": m2})

m3 = int(input("Enter Chemistry Marks : "))
marks.update({"chem": m3})

print(marks)

# Ex 4:- Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
