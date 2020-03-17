def int_func(s):
    return s.title()

symbols = "abcdefghijklmnopqrstuvwxyz "
while True:
    x = input('input numbers with spaces:\n')
#   if not all(char in x for char in symbols): #почему не работает??
    if [x for x in x if x not in symbols]:
        continue
    x = x.split(' ')
    res = []
    for i in range(0, len(x)):
        new_word = int_func(x[i])
        res.append(new_word)
        i+=1
    new_string = ' '.join(res)
    print(new_string)
    break
