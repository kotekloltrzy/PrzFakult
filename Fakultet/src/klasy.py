class Dom:
    def __init__(
        self,
        dlugosc: float,
        szerokosc: float,
        liczba_pieter: int,
        liczba_pokoi: int,
        ilosc_okien: int,
        garaz: bool,
        piwnica: bool,
        poddasze: bool,
        rodzaj: str,
    ):
        self.state = "Dane podane"
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.liczba_pieter = liczba_pieter
        self.ilosc_okien = ilosc_okien
        self.rodzaj = rodzaj
        self.garaz = garaz
        self.piwnica = piwnica
        self.poddasze = poddasze
        self.rodzaj = rodzaj
        self.liczba_pokoi = liczba_pokoi

    def reset(self):
        self.state = "Brak danych"
        self.szerokosc = None
        self.dlugosc = None
        self.liczba_pieter = None
        self.ilosc_okien = None
        self.rodzaj = None
        self.garaz = None
        self.piwnica = None
        self.poddasze = None
        self.rodzaj = None
        self.liczba_pokoi = None


class Poddasze:
    def __init__(self, rodzaj: str, dom):
        self.rodzaj = rodzaj
        self.powierzchnia = dom.szerokosc * dom.dlugosc

    def koszt(self):
        mnoznik = {"mieszkalne": 1, "magazynowe": 0.25}
        koszt_poddasza = mnoznik[self.rodzaj] * 1500 * self.powierzchnia
        return koszt_poddasza


class Garaz:
    def __init__(self, rodzaj: str, ilosc_aut: str):
        self.ilosc_aut = ilosc_aut
        self.rodzaj = rodzaj

    def koszt(self):
        mnoznik_aut = {"1": 1.0, "2": 1.7}
        mnoznik_rodzaju = {"wolnostojący": 1.0, "dobudowany": 0.9}
        return 200000 * mnoznik_aut[self.ilosc_aut] * mnoznik_rodzaju[self.rodzaj]


class Piwnica:
    def __init__(self, rodzaj: str, dom):
        self.rodzaj = rodzaj
        self.dlugosc = dom.dlugosc
        self.szerokosc = dom.szerokosc
        self.powierzchnia = self.szerokosc * self.dlugosc

    def koszt(self):
        mnoznik = {"użytkowa": 1.4, "magazynowa": 1.0}
        return mnoznik[self.rodzaj] * self.powierzchnia * 2000


class Dzialka:
    def __init__(
        self,
        dlugosc: float,
        szerokosc: float,
        ogrodzenie: bool,
        uzbrojenie: bool,
        drzewa: bool,
        rodzaj_gleby: str,
    ):
        self.state = "Dane podane"
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.ogrodzenie = ogrodzenie
        self.uzbrojenie = uzbrojenie
        self.drzewa = drzewa
        self.rodzaj_gleby = rodzaj_gleby

    def reset(self):
        self.state = "Brak danych"
        self.szerokosc = None
        self.dlugosc = None
        self.ogrodzenie = None
        self.uzbrojenie = None
        self.drzewa = None
        self.rodzaj_gleby = None

    def koszt_ogrodzenia(self, standard):
        if not self.ogrodzenie:
            obwod = (self.szerokosc + self.dlugosc) * 2
            cena = {"zwykły": 90, "drogi": 150}
            trudnosc = {"ziemia": 1.0, "glina": 1.5}

            return obwod * cena[standard] * trudnosc[self.rodzaj_gleby]
        else:
            return 0

    def koszt_przygotowania_pod_budowe(self, standard_plotu, ilosc_drzew):
        koszt = self.koszt_ogrodzenia(standard_plotu)
        if not self.uzbrojenie:
            koszt += 7000
        if self.drzewa:
            koszt += 500 * ilosc_drzew
        return koszt
