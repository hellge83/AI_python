def my_func(a, b, c):
    minimal = min(int(a), int(b), int(c))
    return int(a) + int(b) + int(c) - minimal


while True:
    a = input('input 1st number:\n')
    b = input('input 2nd number:\n')
    c = input('input 3rd number:\n')
    if not (a.isdigit() & b.isdigit() & c.isdigit()):
        continue
    res = my_func(a, b, c)
    print(res)
    break