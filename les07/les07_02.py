class Textil:
    def __init__(self):
        self.flow = 0


class Coat(Textil):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def C_flow(self):
        return self.size / 6.5 + 0.5


class Suit(Textil):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def S_flow(self):
        return self.height * 2 + 0.3

coat = Coat(44)
suit = Suit(176)


print(f'Total flow: {round(coat.C_flow) + round(suit.S_flow)}')