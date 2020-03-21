f = open("courses.txt", 'r', encoding='UTF-8')
dict = {}
for line in f:
    line = line.rstrip('\n')
    words = line.split(' ')
    for word in words:
        dict[words[0]] = words[1:]
f.close()

courses = {}
for key, value in dict.items():
    courses[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])

print(dict)
print(courses)