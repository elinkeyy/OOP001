class Augs:
    def __init__(self, nosaukums, daudzums):
        self.nosaukums = nosaukums
        self.daudzums = daudzums

    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami"

class Auglis(Augs):
    def __init__(self, nosaukums, daudzums, seed_count):
        super().__init__(nosaukums, daudzums)
        self.seed_count = seed_count

    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami, {self.seed_count} sēkas uz 10 gramiem"

class Darzenis(Augs):
    def __init__(self, nosaukums, daudzums, alergiju_izraisa):
        super().__init__(nosaukums, daudzums)
        self.alergiju_izraisa = alergiju_izraisa

    def __str__(self):
        alergijas_teksts = "alerģiju izraisa" if self.alergiju_izraisa else "alerģiju neizraisa"
        return f"{self.nosaukums}, {self.daudzums} grami, {alergijas_teksts}"

class Puke(Augs):
    def __init__(self, nosaukums, daudzums, ziedu_skaits):
        super().__init__(nosaukums, daudzums)
        self.ziedu_skaits = ziedu_skaits

    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami, {self.ziedu_skaits} ziedi"

class Recepte:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.augi = []
        self.alergiju_izraisa = False
        self.deriga = True

    def pievienot_augu(self, augs):
        self.augi.append(augs)
        if isinstance(augs, Puke):
            self.deriga = False
        if isinstance(augs, Darzenis) and augs.alergiju_izraisa:
            self.alergiju_izraisa = True

    def kopējais_daudzums(self):
        return sum(augs.daudzums for augs in self.augi)

    def izvada_informaciju(self):
        print(f"Recepte: {self.nosaukums}")
        for augs in self.augi:
            print(f"*{augs}")
        print("###########")
        print("Recepte izraisa alerģiju" if self.alergiju_izraisa else "Recepte alerģiju neizraisa")
        print("Recepte nederīga" if not self.deriga else "Recepte derīga")

augi = [
    Auglis("Āboli", 30, 5),
    Auglis("Banāni", 20, 0),
    Auglis("Apelsīni", 50, 3),
    Auglis("Bumbieri", 40, 4),
    Darzenis("Burkāni", 100, True),
    Darzenis("Kartupeļi", 50, False),
    Darzenis("Sīpoli", 30, True),
    Darzenis("Paprika", 40, False),
    Puke("Rozes", 500, 4),
    Puke("Tulpes", 300, 3)
]

recepte1 = Recepte("Banānu suflē")
recepte1.pievienot_augu(augi[0]) 
recepte1.pievienot_augu(augi[5]) 
recepte1.pievienot_augu(augi[1])  

recepte2 = Recepte("Ratatuille")
recepte2.pievienot_augu(augi[8])  
recepte2.pievienot_augu(augi[4])

recepte1.izvada_informaciju()
print("\n")
recepte2.izvada_informaciju()