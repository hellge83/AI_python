class Division:

    # def __init__(self):
    @staticmethod
    def divbyzero(a, b):
        try:
            return (a / b)
        except ZeroDivisionError:
            return 'Division by zero is not permitted'


# print(Division.divbyzero(4, 0))
while True:
    a = input('input dividend:\n')
    b = input('input divisor:\n')
    if not a.isdigit() & b.isdigit():
        continue
    print(Division.divbyzero(4, 0))
    break