import math as m


class Complex:

    def __init__(self, real, imag = 0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)

    def __truediv__(self, other):
        denominator = other.real*other.real + other.imag*other.imag
        return Complex((self.real*other.real+self.imag*other.imag)/denominator, (self.imag*other.real-self.real*other.imag)/denominator)

    def __abs__(self):
        return Complex(m.sqrt(self.real*self.real + self.imag+self.imag), 0)

    def __conj__(self):
        return Complex(self.real, -self.imag)

    def __str__(self):
        return "(" + str(self.real) + "," + str(self.imag) + ")"
