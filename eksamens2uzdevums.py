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
    def CikStundasKopa(self):
        self.stunduSkaitsNedels=self.pirmaisPrieksmetsKopSkaits+self.otraisPrieksmetsKopSkaits
        return self.stunduSkaitsNedels
ss1=SakumskolasSkolotajs()
ss1.izvade()
vs1=VidusskolasSkolotajs()
vs1.izvade()