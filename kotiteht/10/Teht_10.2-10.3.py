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

    def kerros_ylos(self, kerros):
        while self.atm != kerros and kerros<self.ylin:
            Hissi.tulostus(self)
            self.atm += 1
            if kerros>self.ylin:
                self.atm=self.ylin
                break
            if self.atm == kerros:
                Hissi.tulostus(self)
                print("tääl ollaa")
                break

    def kerros_alas(self, kerros):
        while self.atm != kerros:
            Hissi.tulostus(self)
            self.atm -= 1
            if self.atm == kerros:
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
        for i in range(luku):
           self.hissit.append(Hissi(1, 50, 1))

    def palo(self):
        print("Palohälytys!!")
        for i in self.hissit:
            i.siirry_kerrokseen(self.alin)
            Hissi.tulostus(i)

    def aja(self, numero, kohde):
        elevator = self.hissit[numero - 1]
        print(f"Ajetaan hissiä {numero}\n")
        elevator.siirry_kerrokseen(kohde)


        # Hissi.siirry_kerrokseen(numero, kohde)


kerros = 1
kys = Talo(1, 50, 6, 1)
while kerros < 51:
    hissi_nr=int(input("Valitse hissi"))
    kohde = int(input("Mihin kerrokseen haluat?"))
    if kohde>50 and kohde!=112:
        break
    if kohde == 112:
        kys.palo()
        break
    kys.aja(hissi_nr, kohde)