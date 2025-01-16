class Dzivnieks:
    def __init__(self, vards, kajas):
        self.vards = vards
        self.kajas = kajas
    def skanja(self):
        print("random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kājas"

class Suns(Dzivnieks):
    def __init__(self, vards, kajas):
        super().__init__(vards, kajas)
        self.vards = "Komisārs " + self.vards

d1 = Dzivnieks("Gauja", 4)
print(d1)
d1.skanja()
s1 = Suns("Reksis", 4)
print(s1)
s1.skanja()