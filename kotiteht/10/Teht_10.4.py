import random
class Auto:
    def __init__(self,rekkari,huippu):
        self.rekkari=rekkari
        self.huippu=huippu
        self.atm = 0
        self.matka = 0
        self.aika = 0

    def kiihdytys(self,nopeus):
        self.atm=self.atm+nopeus
        if self.atm>self.huippu:
            self.atm=self.huippu
        elif self.atm<0:
            self.atm=0

    def kuljettu_matka(self,tunnit):
        self.matka+=(self.atm*tunnit)


    def tulostaAuto(self):
        print(self.rekkari, self.atm, self.matka)

    def autojen_luonti(self):
        autot=[]
        for i in range(1, 10):
            autot.append(Auto("ABC-" + str(i),random.randint(100,200)))
        return autot

class Kilpailu:

    def __init__(self,nimi,pituus,autot):
        self.nimi=nimi
        self.pituus=pituus
        self.autot=autot

    def tunti_kuluu(self):
        nopeus=random.randint(-10,15)
        Auto.kiihdytys(autot,nopeus)

    def tulosta_tilanne(self):
        for auto in autot:
            print(Auto.tulostaAuto(auto))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if Auto.kuljettu_matka(auto,tunti) >= self.pituus:
                return True
            else:
                continue

autot = Auto.autojen_luonti()
tunti = 0
romuralli=Kilpailu("Suuri romuralli", 8000,autot)
while True:
    Kilpailu.tunti_kuluu()

    if Kilpailu.kilpailu_ohi():
        print("Kilpailu ohi!\n")
        Kilpailu.tulosta_tilanne()
        break

    else:
        tunti+=1

        if tunti % 10 == 0:
            print(f"Tunti: {tunti}\n")
            Kilpailu.tulosta_tilanne()

        else:
            continue