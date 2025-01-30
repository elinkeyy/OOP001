class skolens:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
        self.sanemtasAtzimes=[]
        self.videjais = 0
    def pievienotAtzimi(self, atzime):
        self.sanemtasAtzimes.append(atzime)
    def izvade(self):
        self.videjais = sum(self.sanemtasAtzimes) / len(self.sanemtasAtzimes)
        print(f"Vārds: {self.vards}, Vecums: {self.vecums};")
        print("Atzīmes:")
        for atzime in self.sanemtasAtzimes:
            print(f"{atzime}")
        print(f"Vidējais:{self.videjais}")

sk1 = skolens("Marija", 18)
sk2 = skolens("Jānis", 17)
sk1.pievienotAtzimi(9)
sk1.pievienotAtzimi(3)
sk2.pievienotAtzimi(7)
sk2.pievienotAtzimi(8)
sk1.izvade()
sk2.izvade()
