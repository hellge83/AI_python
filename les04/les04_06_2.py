from itertools import cycle
import time

tmp = [1, 2, 3, 4, 5]
c = 0
for el in cycle(tmp):
    if c>20:
        break
    print(el)
    time.sleep(1)
    c+=1
