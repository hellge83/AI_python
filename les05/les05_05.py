f = open("new_file.txt", 'x', encoding='UTF-8')
line = input('input numbers with spaces:\n')
f.write(line + '\n')
f.close()

f = open("new_file.txt", 'r', encoding='UTF-8')

for line in f:
    line = line.rstrip('\n')
    number = line.split(' ')

res = sum([int(itm) for itm in number])

print(res)