class Stationery:

    _qty = 0
    _all_tools = []

    def __init__(self, title):
        self.title = title
        Stationery._qty +=1
        Stationery._all_tools.append(self)

    def draw(self):
        return f'{self.title} draw initialization...'


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} draw initialization...'


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} draw initialization...'


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} draw initialization...'


tool1 = Pen('pen')
tool2 = Pencil('pencil')
tool3 = Handle('hahdle')

print(tool1.draw())
print(tool2.draw())
print(tool3.draw())