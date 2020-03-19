from functools import reduce

def mult(*args):
    result = 1
    for itm in args:
        result = result * itm
    return result

data = [itm for itm in range(100, 1002) if not itm % 2]
res = reduce(mult, data)
print(res)