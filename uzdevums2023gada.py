import math
class kubs:
    def ievade(self):
        self.malasGarums = int(input("Ievadiet malas garumu no 2 līdz 10"))
        self.krasasNosaukums = input("Ievadiet kuba krāsu")
    def izvade(self):
        self.aprekinatTilpumu = pow(self.malasGarums, 3)
        print(f"Kuba krāsa - {self.krasasNosaukums}, tilpums - {self.aprekinatTilpumu}")

k1 = kubs()
k1.ievade()
k1.izvade()