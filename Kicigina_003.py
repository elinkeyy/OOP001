from abc import ABC, abstractmethod
class telpa():
    def __init__(self, numurs, platiba, cilvekuDaudzums):
        self.numurs = numurs
        self.platiba = platiba
        self.cilvekuDaudzums = cilvekuDaudzums
    
    def palielinat_cilvekuDaudzums(self, cilveks):
        self.cilvekuDaudzums += cilveks

    @abstractmethod
    def izvade(self):
        pass
    
    
class datorklase(telpa):
    def __init__(self, numurs, platiba, datoruSkaits, cilvekuDaudzums):
        super().__init__(numurs, platiba, cilvekuDaudzums)
        self.datoruSkaits = datoruSkaits
        self.pielautsCilvekuSkaits = self.platiba / 0.8
        self.pielautsDatoruSkaits = 0

    def nepieciesamoCilvekuSkaits(self):
        if self.cilvekuDaudzums > self.pielautsCilvekuSkaits:
            return f"pārāk daudz cilvēku"
        else:
            pass

    def nepieciesamoDatoruSkaits(self):
        if self.pielautsDatoruSkaits == self.cilvekuDaudzums:
            pass
        if self.pielautsDatoruSkaits < self.cilvekuDaudzums:
            return f"nepieciešami papildus datori"

    def izvade(self):
        return f"Datorklase '{self.numurs}', {self.platiba} kvm, {self.datoruSkaits} datori, {self.cilvekuDaudzums} cilvēku, {self.nepieciesamoCilvekuSkaits()}, {self.nepieciesamoDatoruSkaits()}"
    
class kabinets(telpa):
    def __init__(self, numurs, platiba, galduDaudzums, cilvekuDaudzums):
        super().__init__(numurs, platiba, cilvekuDaudzums)
        self.galduDaudzums = galduDaudzums
        self.pielautsCilvekuSkaits = self.platiba /1
        self.pielautsGalduSkaits = 0

    def nepieciesamoCilvekuSkaits(self):
        if self.pielautsCilvekuSkaits < self.cilvekuDaudzums:
            return f"pārāk daudz cilvēku"
        else:
            pass
    def nepieciesamoGalduSkaits(self):
        if self.pielautsGalduSkaits < self.cilvekuDaudzums:
            return f"nepietiek galdu"
        else:
            pass
        
    def izvade(self):
        return f"Kabinets '{self.numurs}', {self.platiba} kvm, {self.galduDaudzums} galdu, {self.cilvekuDaudzums} cilveki, {self.nepieciesamoCilvekuSkaits()}, {self.nepieciesamoGalduSkaits()}"
       
klases = [
    datorklase("34", 12, 20, 43),
    datorklase("54", 45, 21, 22),
    datorklase("24", 10, 10, 12),
    kabinets("27", 12, 12, 10),
    kabinets("30", 30, 24, 40),
    kabinets("15", 15, 25, 20)
]
for telpa in klases:
    print(telpa.izvade())
    