x = input('input numbers with spaces:\n')
x = x.split(' ')
try:
    x = [int(x) for x in x]
    res = [x[i] for i in range(1, len(x)) if x[i]>x[i-1]]
    res.insert(0, x[0]) #первый элемент всегда больше несуществующего для него предыдущего
except ValueError as e:
    print(e)
    raise ValueError(e)

print(res)