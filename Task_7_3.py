class Cell:
    def __init__(self, my_cell):
        self.my_cell = int(my_cell)

    def __add__(self, other):
        return (self.my_cell + other.my_cell)

    def __sub__(self, other):
        if self.my_cell > other.my_cell:
            return (self.my_cell - other.my_cell)
        else:
            return f'Вычитание невозможно'

    def __mul__(self, other):
        return (self.my_cell * other.my_cell)

    def __truediv__(self, other):
        return (self.my_cell // other.my_cell)

    def make_order(self, cell_items):
        row = ''
        for i in range(int(self.my_cell / cell_items)):
            row += f'{"*" * cell_items} \n'
        return row


cell_1 = Cell(25)
cell_2 = Cell(38)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
