def exp(x, y):
    return float(x) ** int(y)


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

