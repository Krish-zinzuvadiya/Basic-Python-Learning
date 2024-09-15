str1 = 'Krish'
str2 = "Krish Zinzuvadiya"
str3 = '''Python'''  # valid in python

print(str1)
print(str2)
print(str3)

# Length Of string
str4 = "Hello World"
print(len(str4))  # prints 11


# String Functions
STR1 = "i am a coder Learning Java"
# returns true if string ends with substr
print(STR1.endswith("er"))

# capitalizes 1st char
print(STR1.capitalize())

# replaces all occurrences of old with new
print(STR1.replace("Java", "Python"))

# returns 1st index of 1st occurrence
print(STR1.find("a"))

# counts the occurrence of substr in string
print(STR1.count("am"))
