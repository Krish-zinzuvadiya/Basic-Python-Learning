import os  # Module
# File I/O :- We have to open a file before reading or writing.
# We can open a file in read mode, write mode, append mode, read and write mode
# We can use 'r', 'w', 'a'.


# Text Files:- .txt, .docx, .log etc.
# Binary Files:- .mp4, .mov, .png, .jpeg etc.


# Open, Read & Close File :- We have to open a file before reading or writing.


# Read...

f = open("demo.txt", "r")  # Works For Write And Delete Also.
data = f.read(5)
list1 = f.readline()
print(data)
print(list1)
print(type(data))
f.close()

# Write...
f1 = open("demo.txt", "a")  # a-append
f1.write("Then I'll Learn FSD")
f1.close()

print("-------")
# With...
with open("demo.txt", "r") as f2:
    data = f2.read()
    print(data)


# Delete :- using the os module
os.remove("demo.txt")  # Delete File
