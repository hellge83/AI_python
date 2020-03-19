import random
data = [random.randint(1, 10) for _ in range(20)]
result = [itm for itm in data if data.count(itm) == 1]
print(result)

