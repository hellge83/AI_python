class Worker:
    _qty = 0
    _all_workers = []

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        Worker._qty +=1
        Worker._all_workers.append(self)



class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

vasya = Position('vasya', 'ivanov', 'qa', 30000, 10000)

print(1)