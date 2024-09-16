# Ex 1:- Create student class that takes name & marks of 3 subjects as arguments in constructor.
#        Then create a method to print the average.
class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum1 = 0
        for i in self.marks:
            sum1 += i
        print("Hi, ", self.name, " Your Avg. Score Is : ", sum1/3)


s1 = Student("Smit", [99, 98, 97])
s1.get_avg()


# Ex 2:- Create Account class with 2 attributes - balance & account no.
#        Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.account_no = acc

    # Debit Method.
    def debit(self, amt):
        self.bal -= amt
        print("Rs.", amt, " Was Debited")
        print("Total Amount : ", self.get_balance())

    # Credit Method.
    def credit(self, amt):
        self.bal += amt
        print("Rs.", amt, " Was Credited")
        print("Total Amount : ", self.get_balance())

    # Get Balance Method.
    def get_balance(self):
        return self.bal


acc1 = Account(10000, 12345)
print(acc1.bal)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
