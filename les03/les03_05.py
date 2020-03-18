def sum_list (lst):

    digits = [int(item) for item in lst]
    sum = 0
    for n in digits:
        sum += n
    return sum

symbols = ".,:;!_*-+()/#¤%&"
res = 0
while True:

    x = input('input numbers with spaces:\n')
    if any(char in symbols for char in x):
        out = "................"
        x = x.translate(str.maketrans(symbols, out))
        x = x.split('.')[0]
        x = x.split(' ')
        x = [x for x in x if x]
        res = res + sum_list(x)
        print(res)
        break
    else:
        x = x.split(' ')
        res = res + sum_list(x)
        print(res)


