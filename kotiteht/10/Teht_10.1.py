class Hissi:

    def __init__(self,alin,ylin,atm):
        self.alin=alin
        self.ylin=ylin
        self.atm=atm

    def siirry_kerrokseen(self,kerros):
        if self.atm<kerros:
            Hissi.kerros_ylos(h)
        elif self.atm>kerros:
            Hissi.kerros_alas(h)
        elif self.atm==kerros:
            print("Tääl ollaa jo >:(")



    def kerros_ylos(self):
        while self.atm!= kerros:
            self.atm+=1
            if self.atm==kerros:
                Hissi.tulostus(h)
                print("tääl ollaa")
    def kerros_alas(self):
        while self.atm!= kerros:
            Hissi.tulostus(h)
            self.atm-=1
            if self.atm==kerros:
                Hissi.tulostus(h)
                print("tääl ollaa")
    def tulostus(self):
        print(self.atm)
h=Hissi(1,7,1)
kerros=1
while kerros <8:
    kerros=int(input("Mihin kerrokseen haluat?"))
    Hissi.siirry_kerrokseen(h,kerros)
