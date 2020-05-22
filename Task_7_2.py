from abc import ABC


class Clothes(ABC):
    def __int__(self, cloth, V, H):
        self.cloth = cloth
        self.V = V
        self.H = H

    @property
    def AllCloth(self, V, H):
        return (V / 6.5 + 0.5) + (2 * H + 0.3)


class Coat(Clothes):
    def CoatCloth(self, V):
        return V / 6.5 + 0.5


class Suit(Clothes):
    def SuitCloth(self, H):
        return 2 * H + 0.3


suit_1 = Suit()
coat_1 = Coat()
print(f'Для костяма требуется: {suit_1.SuitCloth(180):.2f} ткани')
print(f'Для пальто требуется: {coat_1.CoatCloth(50):.2f} ткани')
print(f'Всего требуется: {suit_1.SuitCloth(180) + coat_1.CoatCloth(50):.2f} ткани')
