def exp(x, y):
    y = abs(int(y))
    x = float(x)
    res = 1
    while y >0:
        res = x * res
        y -=1
    return 1 / res


while True:
    try:
        x = input('input positive float:\n')
        y = input('input negative number:\n')
        if (not int(y)>0) & (float(x)>0):
            res = exp(x, y)
            print(res)
        else:
            print('sign mismatched')
            continue
    except ValueError:
        print('not digit')
        continue
    break
