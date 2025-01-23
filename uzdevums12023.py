class csddTransports():
    def ievade(self):
        self.zimols = "BMW"
        self.modelis = "A4"
        self.registracijasDatums = "22.10.2018"
        self.masa = 1000
        self.degvielasVeidaApz = "D"
    def izvade(self):
        print(f"zīmols: {self.zimols} \nmodelis: {self.modelis} \nregistrācijas datums CSDD {self.registracijasDatums} \nmasa(kg) {self.masa} \ndegvielas veids {self.degvielasVeidaApz}")

t1 = csddTransports()
t1.ievade()
t1.izvade()