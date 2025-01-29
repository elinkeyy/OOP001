class Turnirs:
    def __init__(self, nosaukums, cilvekuSkaits, grupuSkaits, sportaVeids):
        self.nosaukums = nosaukums
        self.cilvekuSkaits = cilvekuSkaits
        self.grupuSkaits = grupuSkaits
        self.sportaVeids = sportaVeids
        self.sponsori = []

    def pievienotSponsoru(self, sponsors):
        self.sponsori.append(sponsors)

    def izvade(self):
        sponsoruSaraksts = "\n".join(self.sponsori)
        return (
            f"Šis ir {self.sportaVeids} turnīrs “{self.nosaukums}”, kurā piedalās {self.cilvekuSkaits} cilvēki, {self.grupuSkaits} grupās.\n"
            f"Sponsori:\n{sponsoruSaraksts}"
        )

t1 = Turnirs("Last Dab 2025", 18, 5, "Tortnite")
t1.pievienotSponsoru("Adidaš")
t1.pievienotSponsoru("Mike")
t1.pievienotSponsoru("DolčeNKabana")

t2 = Turnirs("Čempis", 24, 6, "futbola")
t2.pievienotSponsoru("Naik")
t2.pievienotSponsoru("Pantera")
t2.pievienotSponsoru("Adaž")

print(t1.izvade())
print("\n")
print(t2.izvade())