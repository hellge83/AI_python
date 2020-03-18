def div(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return 'Division by zero'


while True:
    a = input('input 1st number:\n')
    b = input('input 2nd number:\n')
    if not (b.isdigit() & a.isdigit()):
        continue
    res = div(a, b)
    print(res)
    break
