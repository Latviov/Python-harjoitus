class Julkaisu:
    def __init__(self,julkaisu_nimi):
        self.julkaisu_nimi=julkaisu_nimi

    def tulostus(self):
        print(self.julkaisu_nimi)

class Kirja(Julkaisu):
    def __init__(self,kirjoittaja,sivut,julkaisu_nimi):
        self.kirjoittaja=kirjoittaja
        self.sivut=sivut
        super().__init__(julkaisu_nimi)

    def tulostus(self):
        super().tulostus()
        print(f"kirjoittaja: {self.kirjoittaja}, sivujen määrä:{self.sivut}")


class Lehti(Julkaisu):
    def __init__(self,editoija,julkaisu_nimi):
        self.editoija=editoija
        super().__init__(julkaisu_nimi)

    def tulostus(self):
        super().tulostus()
        print(f"Editoija {self.editoija}")

if __name__=='__main__':
    kirja = Kirja("Miikka Mäki-Uuro",310,"Python on koville jäbille")
    kirja.tulostus()
    lehti = Lehti("Matti Peltoniemi","SQL ei oo kivaa")
    lehti.tulostus()
