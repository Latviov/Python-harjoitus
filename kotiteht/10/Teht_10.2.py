class Hissi:

    def __init__(self,alin,ylin,atm):
        self.alin=alin
        self.ylin=ylin
        self.atm=atm

    def siirry_kerrokseen(self,kerros):
        if self.atm<kerros:
            Hissi.kerros_ylos(self)
        elif self.atm>kerros:
            Hissi.kerros_alas(self)
        elif self.atm==kerros:
            print("Tääl ollaa jo >:(")


    def kerros_ylos(self):
        while self.atm!= kerros:
            self.atm+=1
            if self.atm==kerros:
                Hissi.tulostus(self)
                print("tääl ollaa")
    def kerros_alas(self):
        while self.atm!= kerros:
            Hissi.tulostus(self)
            self.atm-=1
            if self.atm==kerros:
                Hissi.tulostus(self)
                print("tääl ollaa")
    def tulostus(self):
        print(self.atm)

class Talo:

    def __init__(self,alin,ylin,luku,atm):

        self.alin=alin
        self.ylin=ylin
        self.luku=luku
        self.atm=atm

        self.hissit = []
        for i in range(1, 4):
            self.hissit.append(Hissi(1, 50,1))

    #def palo(self):
    #    if kerros==112:
    #        Hissi.siirry_kerrokseen(self,1)
    #        print("Palohälytys!")
    def aja(self,numero,kohde):
        self.numero=numero
        self.kohde=kohde
        Hissi.siirry_kerrokseen(numero,kohde)



kerros=1
kys=Talo(1,50,3,1)
while kerros <51:
    kohde=int(input("Mihin kerrokseen haluat?"))
    nykyinen=int(input("Missä kerroksessa olet"))
    kys.aja(2, kohde)
    #if kohde==112:
        #Hissi.tulostus(hissi)
