class Skolotajs:
    stunduSkaitsNedels = 0
    skolotajuTips = 0
    uzvards="Nezināms"

class SakumskolasSkolotajs(Skolotajs):
    klase="x.i"
    def __init__(self):
        self.skolotajuTips=1
    def izvade(self):
        print(f"Sākumskolas (tips - {self.skolotajuTips}) māca {self.stunduSkaitsNedels}")

class VidusskolasSkolotajs(Skolotajs):
    pirmaisPrieksmets="x prieksmets"
    otraisPrieksmets="y prieksmets"
    pirmaisPrieksmetsKopSkaits=0
    otraisPrieksmetsKopSkaits=0
    def kopstundas(self):
        self.stunduSkaitsNedels=self.pirmaisPrieksmetsKopSkaits+self.otraisPrieksmetsKopSkaits
        return self.stunduSkaitsNedels
    def izvade(self):
        print(f"Vidusskolas (tips - {self.skolotajuTips}) māca {self.stunduSkaitsNedels}")
def main():

    uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
    klase = input("Ievadiet skolotāja klasi: ")
    stundas = int(input("Ievadiet skolotāja stundu skaitu: "))
    
    sakumskolas_skolotajs = SakumskolasSkolotajs(uzvards, klase, stundas)
    print(sakumskolas_skolotajs.izvade())

    # Input for VidusskolasSkolotajs
    uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
    stundas = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    stundas = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))

ss1=SakumskolasSkolotajs()
ss1.izvade()
vs1=VidusskolasSkolotajs()
vs1.izvade()