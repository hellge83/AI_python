class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def weight(self, m, h):
        res = self._length * self._width * int(m) * int(h) / 1000
        # print(res)
        return res


try:
    sm = input('Input weight per 1 sm: \n')
    road_height = input('input asphalt height: \n')
    road_length = input('Input total lenght: \n')
    road_width = input('Input total width: \n')
    r = Road(int(road_length), int(road_width))
    total_weight = r.weight(sm, road_height)
    print(f'Total weight is: {total_weight} tons')
except ValueError as e:
    print(e)