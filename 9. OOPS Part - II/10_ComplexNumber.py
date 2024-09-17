# Complex numbers have real and imaginary parts....
# Example....
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal, newImg)

    def __sub__(self, other):
        newReal = self.real - other.real
        newImg = self.img - other.img
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

# Adding two complex numbers....
num3 = num1 + num2
num3.showNumber()
# Subtracking two complex numbers....
num4 = num1 - num2
num4.showNumber()
