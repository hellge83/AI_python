f = open("digits.txt", 'r', encoding='UTF-8')
digits = {}
for line in f:
    line = line.rstrip('\n')
    words = line.split(' ')
    for word in words:
        digits[words[0]] = words[2]
f.close()

replace = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три' , 'Four' : 'Четыре'}
d1 = {key: value for key, value in iter(digits.items())}
res = {value: d1[key] for key, value in iter(replace.items())}

f = open("new_digits.txt", 'x', encoding='UTF-8')
for key, value in res.items():
    f.write(f'{key} - {value}\n')

f.close()
