# Ex 1:- WAP to find the sum of first n numbers. (using while)
n = 5
sum1 = 0
i = 1
while i <= n:
    sum1 += i
    i += 1
print("Total Sum :- ", sum1)


# Ex 2:- WAP to find the factorial of first n numbers. (using for)
n = 3
fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial :- ", fact)
