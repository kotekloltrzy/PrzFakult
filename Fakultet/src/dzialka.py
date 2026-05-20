class Dzialka:
    def __init__(self, szerokosc: float, dlugosc: float, ogrodzenie: bool, uzbrojenie: bool,
                 drzewa: bool, rodzaj_gleby: str):
        self.szerokosc = szerokosc
        self.dlugosc = dlugosc
        self.ogrodzenie = ogrodzenie
        self.uzbrojenie = uzbrojenie
        self.drzewa = drzewa
        self.rodzaj_gleby = rodzaj_gleby

    def reset(self):
        self.szerokosc = None
        self.dlugosc = None
        self.ogrodzenie = None
        self.uzbrojenie = None
        self.drzewa = None
        self.rodzaj_gleby = None

    def koszt_ogrodzenia(self, standard):
        if not self.ogrodzenie:
            obwod = (self.szerokosc + self.dlugosc) * 2
            cena = {
                "zwykły": 90,
                "drogi": 150
            }
            trudnosc = {
                "ziemia": 1.0,
                "glina": 1.5
            }

            return obwod * cena[standard] * trudnosc[self.rodzaj_gleby]
        else:
            return 0

    def koszt_przygotowania_pod_budowe(self, standard_plotu, ilosc_drzew):
        koszt = self.koszt_ogrodzenia(standard_plotu)
        if not self.uzbrojenie:
            print("Koszt uzbrojenia działki: 7000 zł")
            koszt += 7000
        if self.drzewa:
            koszt += (500 * ilosc_drzew)
            print(f"Koszt wycinki {ilosc_drzew} drzew: {500 * ilosc_drzew} zł")
        print(f"Koszt ogrodzenia: {self.koszt_ogrodzenia(standard_plotu)} zł")
        return koszt
