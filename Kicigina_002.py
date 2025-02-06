class autovaditajs:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
        self.masinasNum = []
        self.sodaPunkti = 0
    def pievienot_masinasNum(self, masina):
        self.masinasNum.append(masina)
    def pievienot_sodaPunktus(self, punkti):
        self.sodaPunkti += punkti
    def izvade(self):
        print(f"Vārds: {self.vards}; Vecums: {self.vecums} gadi")
        print(f"Automašīnas īpašumā({len(self.masinasNum)})")
        for masina in self.masinasNum:
            print(f"{masina}")
        print(f"Soda punkti:{self.sodaPunkti}")
m1 = autovaditajs("Emīls", 26)
m2 = autovaditajs("Jana", 56)
m1.pievienot_masinasNum("NL-1331")
m1.pievienot_masinasNum("GR-34")
m2.pievienot_masinasNum("14YOU")
m2.pievienot_masinasNum("14ME")
m1.pievienot_sodaPunktus(4)
m2.pievienot_sodaPunktus(4)
m1.izvade()
m2.izvade()
