import time
from itertools import cycle


class TrafficLight():

    def __init__(self):
        self.__color = {'red': 7, 'yellow': 2, 'green': 7}

    def running(self):
        print('TrafficLight is running:')
        i = 0
        for key, value in cycle(self.__color.items()):
            if i > 10:
                break
            i += 1
            print(key)
            time.sleep(value)


a = TrafficLight()
a.running()