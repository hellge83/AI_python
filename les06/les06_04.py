class Car:

    _qty = 0
    _all_cars = []

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car._qty +=1
        Car._all_cars.append(self)

    def go(self):
        return f'Car is going'

    def stop(self):
        return f'Car stopped'

    def turn(self, direction):
        return f'turned {direction}'

    def show_speed(self):
        return f'Current speed: {self.speed}'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            msg = f'Car speed {self.speed} is higher than allowed'
        else:
            msg = f'Current speed: {self.speed}'
        return msg


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            msg = f'Car speed {self.speed} is higher than allowed'
        else:
            msg = f'Current speed: {self.speed}'
        return msg

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


smart = TownCar(60, 'black', 'smart', False)
porsche = SportCar(100, 'red', 'porsche', False)
gaz = WorkCar(50, 'yellow', 'gaz', False)
ford = PoliceCar(80, 'white', 'ford', True)


print(f'Is {ford.name} a police car? {ford.is_police}')
print(f'Speed message: {gaz.show_speed()}')
print(f'{porsche.name} status: {porsche.go()}')
print(f'{smart.name} {smart.turn("right")}')