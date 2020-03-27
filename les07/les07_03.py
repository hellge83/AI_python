class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        try:
            if abs(self.qty - other.qty) > 0:
                return Cell(self.qty - other.qty)
            else:
                return Cell(0)
        finally:
            if abs(self.qty - other.qty) == 0:
                print('Empty result:')

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(self.qty // other.qty)

    def make_order(self, cols):
        row = ''
        for i in range(self.qty // cols):
            row += f'{"*" * cols} \n'
        row += f'{"*" * (self.qty % cols)}'
        return row

cell1 = Cell(12)
cell2 = Cell(12)

print((cell1 + cell2).qty)
print((cell1 - cell2).qty)
print((cell1 * cell2).qty)
print((cell1 / cell2).qty)
print(cell1.make_order(5))