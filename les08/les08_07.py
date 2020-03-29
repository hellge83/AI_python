class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return Complex(a, b)

    def __str__(self):
        return f'{self.a} + {self.b} * i'


c1 = Complex(1, -2)
c2 = Complex(3, 4)
print(f' c1 = {c1}')
print(f' c2 = {c2}')
print(f' c1 + c2 = {c1 + c2}')
print(f' c1 * c2 = {c1 * c2}')
