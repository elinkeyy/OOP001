import math
from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, krasa, x, y):
        self.krasa = krasa
        self.x = x
        self.y = y
    
    @abstractmethod
    def laukums(self):
        pass
    @abstractmethod
    def perimetrs(self):
        pass

class kvadrats(Figura):
    def __init__(self, krasa, x, y, mala):
        super().__init__(krasa, x, y)
        self.mala = mala
    def laukums(self):
        return self.mala**2
    def perimetrs(self):
        return self.mala*4
    def __str__(self):
        return f"Kvadrāts, krasa = {self.krasa}, koordinātas = ({self.x}, {self.y}), mala = {self.mala}, laukums = {self.laukums()}, perimetrs = {self.perimetrs()}"

class aplis(Figura):
    def __init__(self, krasa, x, y, radiuss):
        super().__init__(krasa, x, y)
        self.radiuss = radiuss
    def laukums(self):
        return math.pi*self.radiuss**2
    def perimetrs(self):
        return 2*math.pi*self.radiuss
    def __str__(self):
        return f"Aplis, krasa ={self.krasa}, koordinātas = ({self.x}, {self.y}), radiuss = {self.radiuss} laukums = {self.laukums()}, perimetrs = {self.perimetrs()}"

figuras = [
    kvadrats('sarkans', 4, 6, 8),
    kvadrats("zils", 6, 89, 43),
    aplis('roza', 76, 56, 34),
    aplis('zaļš', 87, 34, 12)
]
for figura in figuras:
    print(figura)