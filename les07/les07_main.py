import random
from abc import ABC, abstractmethod

human = {
    'name': 'vasya',
    'surname': 'ivanov'
}
# def my_deco(func):
#     def run(*args):
#         print(f'Start {func.__name__}', args)
#         result = func(*[x * 2 for x in args])
#         print(f'End {func.__name__}')
#         return result
#     return run
#
# @my_deco
# def my_f(a: int):
#     return a ** 2
#
# @my_deco
# def my_f_two(a, b):
#     return a, b

class BaseHomo(ABC):
    @abstractmethod
    def ask_name(self):
        pass

class HomoSapience(BaseHomo):
    _population = 0
    _all_homo = []

    def __init__(self):
        self.age = 0
        self.eyes_color = random.choice(('red', 'green', 'blue'))
        HomoSapience._population +=1
        HomoSapience._all_homo.append(self)

    def ask_secret(self):
        print('UAAAH')




class Human(HomoSapience):

    # name: str = ''
    # surname: str = None

    def __init__(self, name, surname):
        super().__init__()
        self.name = name
        self.surname = surname
        self.eyes_color = random.choice(('red', 'green', 'blue', 'brown'))
        self.__secret = len(f'{self.name} {self.surname}')
        self.tmp = []
        # Human._population +=1
        # Human.__all_people.append(self)

    @property
    def secret(self):
        return self.__secret

    @secret.setter
    def secret(self, value):
        self.__secret = value ** 2
        # print(1)

    def ask_name(self):
        print(f'{self.name} {self.surname}')

    def __add__(self, other):
        father = self
        mother = other

        return type(father)(mother.name, father.surname)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def breeding(self, other):
        father = self
        mother = other

        return type(father)(mother.name, father.surname)

    def __call__(self, a):
        self.tmp.append(a)
        return sum(self.tmp)

class Wolf:
    def __init__(self):
        self.tooth = 24
        self.is_alfa = random.choice((True, False))

    def moon(self):
        print('UUUUUUUUu')

class WereWolf(Human, Wolf):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        Wolf.__init__(self)

    def __del__(self):
        print('Im del')

# a = my_f(2)
# b = my_f_two(2, 5)
# print(1)
def my_f(self):
    return self.surname


class GarIter:
    def __init__(self, *obj):
        self.obj = (*obj[0], *obj[1])
        self.num = 0

    def __next__(self):
        if self.num < len(self.obj):
            self.num +=1
            return self.obj[self.num - 1]
        else:
            raise StopIteration

class Garage:
    __iter = GarIter
    def __init__(self, name):
        self.name = name
        self.__box = [1, 2, 3, 4, 5, 6]
        self.__box2 = ['e', 'r']

    def __iter__(self):
        # return self.__box.__iter__()
        return self.__iter(self.__box, self.__box2)



# gar = Garage('monkey')
#
# for itm in gar:
#     print(itm)

# anatoly = WereWolf('tolik', 'sharikov')
# anatoly = None


vasya = Human('vasya', 'ivanov')
vasya.secret = 16
setattr(Human, 'my_f', my_f)
petya = Human('petya', 'petrov')
child = vasya + petya
child2 = vasya.__add__(petya)


print(1)