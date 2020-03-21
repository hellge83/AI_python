f = open("my_file.txt", 'r', encoding='UTF-8')
users = {}
for line in f:
    line = line.rstrip('\n')
    words = line.split(' ')
    for word in words:
        users[words[0]] = words[1]

res = {key: value for key, value in users.items() if int(value) > 20000}
rich = (' ').join(res.keys())

avg = sum({int(value) for key, value in users.items()})/len(users)

print(f'Salary over 20K: {rich}')
print(f'Average salary is {avg}')

f.close()

