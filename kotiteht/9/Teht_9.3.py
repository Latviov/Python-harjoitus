class auto:
    def __init__(self, rekkari, huippu, atm, matka):
        self.rekkari = rekkari
        self.huippu = huippu
        self.atm = atm
        self.matka = matka

    def tulostaAuto(self):
        print(self.rekkari, self.huippu, self.atm, self.matka)

    def kiihdytys(self):
        UusiAuto.atm=UusiAuto.atm+x
        if UusiAuto.atm>UusiAuto.huippu:
            UusiAuto.atm=142
        if UusiAuto.atm<0:
            UusiAuto.atm=0

    def kuljettumatka(self):
        tunti=3
        UusiAuto.matka=UusiAuto.matka+(UusiAuto.atm*tunti)


UusiAuto = auto("ABC-123", 142, 0, 0)

kerrat=3
while kerrat >= 0:
    if kerrat==3:
        x=30
        auto.kiihdytys(x)
        kerrat-=1
    elif kerrat==2:
        x=70
        auto.kiihdytys(x)
        kerrat-=1
    elif kerrat==1:
        x=50
        auto.kiihdytys(x)
        kerrat=0
        break

UusiAuto.kuljettumatka()
UusiAuto.tulostaAuto()
x = -200
auto.kiihdytys(x)
UusiAuto.tulostaAuto()