class skolens:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums
        self.sanemtasAtzimes = []
        self.vid_atzime = 0

    def pievienot_atzimi(self, atzime):
        self.atzime = atzime
        self.sanemtasAtzimes.append(atzime)
    def izvade(self):
        print(f"Vārds: {self.vards}; vecums {self.vecums} gadi;")
        print("Atzīmes:")
        for atzime in self.sanemtasAtzimes:
            print(f"{atzime}")
        self.vid_atzime = sum(self.sanemtasAtzimes)/len(self.sanemtasAtzimes)
        print(f"Vidējais: {self.vid_atzime}")

s1 = skolens("Jānis", 15)
s2 = skolens("Jana", 19)
s1.pievienot_atzimi(67)
s1.pievienot_atzimi(65)
s2.pievienot_atzimi(87)
s2.pievienot_atzimi(56)
s1.izvade()
s2.izvade()