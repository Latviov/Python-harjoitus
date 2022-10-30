class Hissi:
    def __init__(self, alin, ylin, atm):
        self.alin = alin
        self.ylin = ylin
        self.atm = atm

    def siirry_kerrokseen(self, kerros):
        if self.atm < kerros:
            Hissi.kerros_ylos(self, kerros)
        elif self.atm > kerros:
            Hissi.kerros_alas(self, kerros)

    def kerros_ylos(self, floor):
        while self.atm != floor and floor<self.ylin:
            Hissi.tulostus(self)
            self.atm += 1
            if floor<self.ylin:
                self.atm=self.ylin
            if self.atm == floor:
                Hissi.tulostus(self)
                print("tääl ollaa")

    def kerros_alas(self, floor):
        while self.atm != floor:
            Hissi.tulostus(self)
            self.atm -= 1
            if self.atm == floor:
                Hissi.tulostus(self)
                print("tääl ollaa")

    def tulostus(self):
        print(self.atm)


class Talo:

    def __init__(self, alin, ylin, luku, atm):
        self.alin = alin
        self.ylin = ylin
        self.luku = luku
        self.atm = atm
        self.hissit = []
        for i in range(1, 4):
           self.hissit.append(Hissi(1, 50, 1))

    def palo(self):
        for i in self.hissit:
            i.siirry_kerrokseen(self.alin)
            print("Palohälytys!!")
    def aja(self, numero, kohde):
        elevator = self.hissit[numero - 1]
        print(f"Ajetaan hissiä {numero}\n")
        if kohde == 112:
            self.palo()
        elevator.siirry_kerrokseen(kohde)

        # Hissi.siirry_kerrokseen(numero, kohde)


kerros = 1
kys = Talo(1, 50, 3, 1)
while kerros < 51:
    hissi_nr=int(input("Valitse hissi"))
    kohde = int(input("Mihin kerrokseen haluat?"))
    kys.aja(hissi_nr, kohde)