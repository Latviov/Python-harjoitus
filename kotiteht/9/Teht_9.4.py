import random
class auto:
    def __init__(self, rekkari, huippu, atm, matka):
        self.rekkari = rekkari
        self.huippu = random.randint(100, 200)
        self.atm = atm
        self.matka = matka

    def tulostaAuto(self):
        print(self.rekkari, self.huippu, self.atm, self.matka)

    def kiihdytys(self):
        y.atm= y.atm + x
        if y.atm>y.huippu:
            y.atm=y.huippu
        if y.atm<0:
            y.atm=0


    def kuljettumatka(self):
        tunti=1

        y.matka= y.matka+(y.atm * tunti)


pl=1
autot=[]
while pl <=10:
    rekkari=f"ABC-{pl}"
    #ky = random.randint(100, 200)
    y=auto(rekkari,0,0,0)
    y.tulostaAuto()
    pl+=1


kisa=10000

while y.matka<kisa:
    x=random.randint(-10,15)
    auto.kiihdytys(x)
    auto.kuljettumatka(y)
    auto.tulostaAuto(y)