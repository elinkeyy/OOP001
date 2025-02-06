from abc import ABC, abstractmethod
import math
class figura(ABC):
    def __init__(self, krasa, x, y):
        self.krasa = krasa
        self.c_x= x
        self.c_y= y
    @abstractmethod
    def laukums(self):
        pass
    @abstractmethod
    def perimetrs(self):
        pass
class kvadrats(figura):
    def __init__(self, krasa, x, y, mala):
        super().__init__(krasa, x, y)
        self.mala = mala
    def laukums(self):
        self.laukums = self.mala**2
    def perimetrs(self):
        self.perimetrs = self.mala*4
    def __str__(self):
        return f"Kvadrāts({self.c_x}, {self.c_y}), mala = {self.mala}, laukums = {self.laukums()}, perimetrs = {self.perimetrs};"
class aplis(figura):
    def __init__(self, krasa, x, y, radiuss):
        super().__init__(krasa, x, y)
        self.radiuss=radiuss
    def laukums(self):
        return math.pi*self.radiuss**2
    def perimetrs(self):
        return 2*math.pi*self.radiuss
    def __str__(self):
        return f"Aplis ({self.c_x, self.c_y}), radiuss={self.radiuss}, laukums={self.laukums}, perimetrs={self.perimetrs};"

figuras = [
    kvadrats('sarkans', 4, 6, 8),
    kvadrats("zils", 6, 89, 43),
    aplis('roza', 76, 56, 34),
    aplis('zaļš', 87, 34, 12)
]
for figura in figuras:
    print(figura)