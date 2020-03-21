import json
f = open("firms.txt", 'r', encoding='UTF-8')
firms = {}
for line in f:
    line = line.rstrip('\n')
    words = line.split(' ')
    for word in words:
        firms[words[0]] = words[1:]
f.close()

rev = {}
for key, value in firms.items():
    rev[key] = int(value[1]) - int(value[2])

profit = []
lost = []
for value in rev.values():
    if value >=0:
        profit.append(value)
    else:
        lost.append(value)

result = []
result.append(rev)
result.append({'avg_profit': sum(profit)/len(profit)})
result.append({'avg_lost': sum(lost)/len(lost)})

with open("firms.json", "w") as write_f:
    json.dump(result, write_f)