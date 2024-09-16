# Range() In Loop :- Range functions returns a sequence of numbers, starting from 0 by default,
#                    and increments by1 (by default), and stops before a specified number.

for i in range(10):  # range(stop)--> Condition
    print(i)
print("----------")

for i1 in range(2, 10):  # range(start, stop)
    print(i1)

print("----------")
for i2 in range(2, 10, 2):  # range(start,stop,step)
    print(i2)
