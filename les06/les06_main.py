import random

human = {
    'name': 'vasya',
    'surname': 'ivanov'
}


class HomoSapience:
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
        # Human._population +=1
        # Human.__all_people.append(self)


    def ask_secret(self):
        print(self.__secret)

    def ask_name(self):
        print(f'{self.name} {self.surname}')

    def breeding(self, other):
        father = self
        mother = other

        return type(father)(mother.name, father.surname)


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



vasya = Human('vasya', 'ivanov')
petya = Human('petya', 'petrov')

anatoly = WereWolf('tolik', 'sharikov')

print(1)