class Complex_num:
    def __init__(self, index_1, index_2, ):
        self.index_1 = index_1
        self.index_2 = index_2

    def __add__(self, other):
        if self.index_2 + other.index_2 < 0:
            return f'({self.index_1 + other.index_1}{self.index_2 + other.index_2}j)'
        else:
            return f'({self.index_1 + other.index_1}+{self.index_2 + other.index_2}j)'

    def __mul__(self, other):
        if self.index_2 * other.index_1 < 0:
            return f'({self.index_1 * other.index_1 - (self.index_2 * other.index_2)}{self.index_2 * other.index_1}j)'
        else:
            return f'({self.index_1 * other.index_1 - (self.index_2 * other.index_2)}+{self.index_2 * other.index_1}j)'


num_1 = Complex_num(1, 4)
num_2 = Complex_num(-9, 12)
print(num_1 + num_2)
print(num_1 * num_2)
