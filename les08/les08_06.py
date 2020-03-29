class Warehouse:
    _total = 0
    _cost = 0
    _models = set()
    _departments = set()

    def __init__(self):
        self.wh_unit = {'department': '', 'item': '', 'model': '', 'price': '', 'amount': ''}

    @staticmethod
    def digit_validation(itm):
        try:
            int(itm)
            return True
        except ValueError:
            print('It\'s not a digit')
            return False

    @staticmethod
    def params_validation(itm, param):
        params = {'item': ['printer', 'scanner', 'copier'], 'department': ['it', 'accounting', 'office'], 'model': ['hp', 'canon', 'xerox']}

        if itm in params[str(param)]:
            return True
        else:
            print('Wrong input')
            return False

    @staticmethod
    def create_unit():
        unit = []
        string_check = ''
        digit_check = ''

        while not string_check:
            param = input('input device type (printer, copier, scanner):\n')
            string_check = Warehouse.params_validation(param, 'item')
        unit.append(param)
        string_check = ''

        while not string_check:
            param = input('input device model (hp, canon, xerox):\n')
            string_check = Warehouse.params_validation(param, 'model')
        unit.append(param)
        string_check = ''

        while not digit_check:
            param = input('input device price:\n')
            digit_check = Warehouse.digit_validation(param)
        unit.append(int(param))
        digit_check = ''

        while not digit_check:
            param = input('input number of items:\n')
            digit_check = Warehouse.digit_validation(param)
        unit.append(int(param))
        digit_check = ''

        while not string_check:
            param = input('input department (it, accounting, office):\n')
            string_check = Warehouse.params_validation(param, 'department')
        unit.append(param)
        string_check = ''

        if unit[0] == 'printer':
            device = Printer(*unit)
        elif unit[0] == 'scanner':
            device = Scanner(*unit)
        elif unit[0] == 'copier':
            device = Copier(*unit)

        return device


    def new_unit(self):
        self.wh_unit.update(self.unit)
        # print(self.unit)
        Warehouse._total += int(self.wh_unit['amount'])
        Warehouse._cost += (int(self.wh_unit['price']) * int(self.wh_unit['amount']))
        Warehouse._departments.add(self.wh_unit['department'])
        Warehouse._models.add(self.wh_unit['model'])


class Printer(Warehouse):

    def __init__(self, item, name, price, qty, department):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty
        self.department = department
        self.item = item
        self.unit = {'department': department, 'item': item, 'model': name, 'price': price, 'amount': qty}


class Scanner(Warehouse):

    def __init__(self, item, name, price, qty, department):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty
        self.department = department
        self.item = item
        self.unit = {'department': department, 'item': 'scanner', 'model': name, 'price': price, 'amount': qty}


class Copier(Warehouse):

    def __init__(self, item, name, price, qty, department):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty
        self.department = department
        self.item = item
        self.unit = {'department': department, 'item': 'copier', 'model': name, 'price': price, 'amount': qty}


answer = ''
i = 0
while answer != 'n':
    globals()['rec_'+str(i)] = Warehouse.create_unit()
    globals()['rec_'+str(i)].new_unit()
    i+=1
    answer = input('Do you want to add another one? (y/n):\n')


print(f'Total items: {Warehouse._total}')
print(f'Total departments: {Warehouse._departments}')
print(f'Total models: {Warehouse._models}')
print(f'Total cost: {Warehouse._cost}')
