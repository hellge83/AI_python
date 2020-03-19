from itertools import cycle, count
import time

c = 0
for el in cycle(count(7)):
    if c>20:
        break
    print(el)
    time.sleep(1)
    c+=1