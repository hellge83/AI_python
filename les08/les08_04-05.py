class Warehouse:
    # _units = []
    _total = 0
    _cost = 0
    _models = set()
    _departments = set()

    def __init__(self):
        self.wh_unit = {'department': '', 'item': '', 'model': '', 'price': '', 'amount': ''}
        # Warehouse._units.append(self.wh_unit)

    def new_unit(self):
        self.wh_unit.update(self.unit)
        # print(self.unit)
        Warehouse._total += self.wh_unit['amount']
        Warehouse._cost += (self.wh_unit['price'] * self.wh_unit['amount'])
        Warehouse._departments.add(self.wh_unit['department'])
        Warehouse._models.add(self.wh_unit['model'])


class Printer(Warehouse):

    def __init__(self, name, price, qty, department):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty
        self.department = department
        self.item = 'printer'
        self.unit = {'department': department, 'item': 'printer', 'model': name, 'price': price, 'amount': qty}


class Scanner(Warehouse):

    def __init__(self, name, price, qty, department):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty
        self.department = department
        self.item = 'scanner'
        self.unit = {'department': department, 'item': 'printer', 'model': name, 'price': price, 'amount': qty}


class Copier(Warehouse):

    def __init__(self, name, price, qty, department):
        super().__init__()
        self.name = name
        self.price = price
        self.qty = qty
        self.department = department
        self.item = 'copier'
        self.unit = {'department': department, 'item': 'printer', 'model': name, 'price': price, 'amount': qty}


unit1 = Printer('hp', 1000, 2, 'it')
unit2 = Scanner('canon', 2000, 2, 'accounting')
unit3 = Copier('xerox', 3000, 3, 'office')

unit1.new_unit()
unit2.new_unit()
unit3.new_unit()

print(f'Total items: {Warehouse._total}')
print(f'Total departments: {Warehouse._departments}')
print(f'Total models: {Warehouse._models}')
print(f'Total cost: {Warehouse._cost}')
