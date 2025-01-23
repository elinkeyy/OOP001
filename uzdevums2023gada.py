import math
class kubs:
    def ievade(self):
        self.malasGarums = int(input("Ievadiet malas garumu no 2 līdz 10"))
        self.krasasNosaukums = input("Ievadiet kuba krāsu")
    def izvade(self):
        self.aprekinatTilpumu = pow(self.malasGarums, 3)
        print(f"Kuba krāsa - {self.krasasNosaukums}, tilpums - {self.aprekinatTilpumu} cm kubā")
    def kubg(self):
        self.krasasNosaukums = "zaļa"
        self.malasGarums = 10
        print(f"kubg krāsa - {self.krasasNosaukums}, malas garums - {self.malasGarums} cm")
    def kubr(self):
        self.krasasNosaukums = "sarkana"
        self.malasGarums = 1
        print (f"kubr krāsa - {self.krasasNosaukums}, malas garums - {self.malasGarums} cm")
    del kubr

k1 = kubs()
k1.ievade()
k1.izvade()
k1.kubg()
k1.kubr()