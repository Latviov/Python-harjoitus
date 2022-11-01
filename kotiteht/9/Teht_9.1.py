class auto:
    def __init__(self, rekkari,huippu,atm,matka ):
        self.rekkari = rekkari
        self.huippu=huippu
        self.atm=atm
        self.matka=matka

    def tulostaAuto(self):
        print(self.rekkari,self.huippu, self.atm, self.matka)

UusiAuto = auto("ABC-123", 142,0,0)
VanhaAuto=auto("XYZ-123",270,0,0)

UusiAuto.tulostaAuto()
VanhaAuto.tulostaAuto()