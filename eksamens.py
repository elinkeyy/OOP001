class Doktorats:
    def __init__(self, nosaukums='N/A', pacientuSkaits=0):
        self.nosaukums = nosaukums
        self.pacientuSkaits = pacientuSkaits
    def ievade(self):
        self.nosaukums=input("Ievadiet nosaukumu")
        try:
            self.pacientuSkaits = int(input("Ievadiet pacientu skaitu"))
        except:
            self.pacientuSkaits = 0
        finally:
            print("Ievade veiksmīga:", self.pacientuSkaits)

    def izvade(self):
        print(f"Doktorats {self.nosaukums} apkalpo - {self.pacientuSkaits}")
d1=Doktorats("Ziemels", 325)
d1.izvade()
d1.ievade()
d1.izvade()
print(d1)
d2=Doktorats('Bērziņš', 32)
d2.izvade()
d2.ievade()
d2.izvade()