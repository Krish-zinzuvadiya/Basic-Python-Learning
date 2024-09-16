# Ex 1:- Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")


# Ex 2:- WAF that replace all occurrences of “java” with “python” in above file.
# using Ex 1...
def check():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Java", "Python")
    print(new_data)
    with open("practice.txt", "w") as f:
        f.write(new_data)


check()


# Ex 3:- Search if the word “learning” exists in the file or not.
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (word in data):
        print("Found")
    else:
        print("Not Found")


# Ex 4:- WAF to find in which line of the file does the word “learning”occur first.
#        Print -1 if word not found.
def check_line():
    word1 = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word1 in data):
                print("The word is found in line no. : ", line_no)
                return
            line_no += 1
    return -1


check_line()


# Ex 5:- From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("number.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

print(count)
