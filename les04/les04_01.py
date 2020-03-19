import sys

def f(a, b, c):
    return (a * b) + c


_, hours, rate, bonus, *c = sys.argv

try:
    hours, rate, bonus = float(hours), float(rate), float(bonus)
except ValueError as e:
    print(e)
    raise ValueError(e)

print(f(hours, rate, bonus))