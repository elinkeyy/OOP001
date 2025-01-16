from abc import ABC, abstractmethod

class Dzivnieks:
    def __init__(self, vards, kajas):
        self.vards = vards
        self.kajas = kajas
    @abstractmethod
    def skanja(self):
        print("random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kājas"

class Suns(Dzivnieks):
    def __init__(self, vards, kajas):
        super().__init__(vards, kajas)
        self.vards = "Komisārs " + self.vards
    def skanja(self):
        print("Vau! Vau! Gaf! Gaf!")

class Kakis(Dzivnieks):
    def __init__(self, vards, kajas):
        super().__init__(vards, kajas)
        self.vards = "Mans " + self.vards
    def skanja(self):
        print("Meow!")
class Govs(Dzivnieks):
    def skanja(self):
        print("MUUUUU")

d1 = Dzivnieks("Gauja", 4)
print(d1)
d1.skanja()
s1 = Suns("Reksis", 4)
print(s1)
s1.skanja()
k1= Kakis("Pups", 4)
print(k1)
k1.skanja()
dzivniekuSaraksts = []
dzivniekuSaraksts.append(Suns("Reksis", 3))
dzivniekuSaraksts.append(Suns("Volvis", 4))
dzivniekuSaraksts.append(Suns("Caps", 4))
dzivniekuSaraksts.append(Kakis("Murcis", 4))
dzivniekuSaraksts.append(Kakis("Burkāns", 4))
dzivniekuSaraksts.append(Govs("Gauja", 4))

print("###############")
for dzivnieks in dzivniekuSaraksts:
    print(dzivnieks)
    dzivnieks.skanja()
