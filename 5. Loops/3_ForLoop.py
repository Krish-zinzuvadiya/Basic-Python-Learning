# Loops :- Loops are used used for sequential traversal. For traversing list, string, tuples etc.

# For Loop...

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

str1 = "KrishZinzuvadiya"

for char in str1:
    if (char == 'n'):
        print("n found")
        break
    print(char)
else:
    print("END")
