def fibo_gen():
    res = 1
    for i in range(0, 15):
        if i == 0: #0!=1
            yield 1
            i+=1
        else:
            res *=i
            yield res


for el in fibo_gen():
     print(el)
