class Skolotajs:
    stunduSkaitsNedels = 0
    skolotajuTips = 0
    uzvards="Nezināms"

class SakumskolasSkolotajs(Skolotajs):
    klase="x.i"
    def __init__(self):
        self.skolotajuTips=1
    def ievade(self):
        self.uzvards = input("Ievadiet uzvardu")
        self.klase = (input("Ievadiet klasi"))
        self.stunduSkaitsNedels = int(input("Ievadiet stundu skaitu nedeļā!"))
    def izvade(self):
        print(f"Sākumskolas (tips - {self.skolotajuTips}) skolotājs {self.uzvards} māca {self.stunduSkaitsNedels}")

class VidusskolasSkolotajs(Skolotajs):
    pirmaisPrieksmets="x prieksmets"
    otraisPrieksmets="y prieksmets"
    pirmaisPrieksmetsKopSkaits=0
    otraisPrieksmetsKopSkaits=0
    def __init__(self):
        self.skolotajuTips=3
    def kopstundas(self):
        self.stunduSkaitsNedels = self.pirmaisPrieksmetsKopSkaits+self.otraisPrieksmetsKopSkaits
        return self.stunduSkaitsNedels
    def ievade(self):
        self.uzvards = input("Ievadiet vidusskolas skolotāja uzvardu")
        self.pirmaisPrieksmets = input("Ievadiet pirmo priekšmetu!")
        self.pirmaisPrieksmetsKopSkaits = int(input("Uzraksties pirmā priekšmeta stundu skaitu!"))
        self.otraisPrieksmets = input("Ievadiet otrā priekšmetu!")
        self.otraisPrieksmetsKopSkaits = int(input("Uzrakstiet otrā priekšmeta stundu skaitu!"))

    def izvade(self):
        print(f"Vidusskolas (tips - {self.skolotajuTips}) skolotājs {self.uzvards} māca šīs priekšmetus:{self.pirmaisPrieksmets} un {self.otraisPrieksmets}, kopā {self.kopstundas()}")

#ss1=SakumskolasSkolotajs()
#ss1.ievade()
#ss1.izvade()
vs1=VidusskolasSkolotajs()
vs1.ievade()
vs1.izvade()