class figura:
    def __init__(self, nosaukums, krasa, x, y, mala):
        self.nosaukums = nosaukums
        self.krasa = krasa
        self.c_x= x
        self.c_y= y
        self.mala = mala
class kvadrats(figura):
    def __init__(self, mala, x, y, laukums, perimetrs):
        super().__init__(mala, x, y, laukums, perimetrs)
        self.laukums = laukums
        self.perimetrs = perimetrs
    def laukumsUnPerimetrs(self, laukums, perimetrs, mala):
        super().__init__(mala, laukums, perimetrs)
        self.laukums = pow(self.mala, 2)
        self.perimetrs = self.mala*4
    def izvade(self):
        print(f"Kvadrāts({self.c_x}, {self.c_y}), mala = {self.mala}, laukums = {self.laukums}, perimetrs = {self.perimetrs};")


k1= kvadrats()
k1.izvade()