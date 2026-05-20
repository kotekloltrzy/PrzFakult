class Dom:
    def __init__(self, szerokosc: float, dlugosc: float, liczba_pieter: int, ilosc_okien: int, garaz: bool,
                 piwnica: bool, poddasze: bool, rodzaj: str):
        self.szerokosc = szerokosc
        self.dlugosc = dlugosc
        self.liczba_pieter = liczba_pieter
        self.ilosc_okien = ilosc_okien
        self.rodzaj = rodzaj
        self.garaz = garaz
        self.piwnica = piwnica
        self.poddasze = poddasze
        self.rodzaj = rodzaj

    def reset(self):
        self.szerokosc = None
        self.dlugosc = None
        self.liczba_pieter = None
        self.ilosc_okien = None
        self.rodzaj = None
        self.garaz = None
        self.piwnica = None
        self.poddasze = None
        self.rodzaj = None


class Poddasze:
    def __init__(self, rodzaj: str, dom):
        self.rodzaj = rodzaj
        self.powierzchnia = dom.szerokosc * dom.dlugosc

    def koszt(self):
        mnoznik = {
            "mieszkalne": 1,
            "magazynowe": 0.25
        }
        koszt_poddasza = mnoznik[self.rodzaj] * 1500 * self.powierzchnia
        return koszt_poddasza


class Garaz:
    def __init__(self, rodzaj: str, ilosc_aut: str):
        self.ilosc_aut = ilosc_aut
        self.rodzaj = rodzaj

    def koszt(self):
        mnoznik_aut = {
            "1": 1.0,
            "2": 1.7
        }
        mnoznik_rodzaju = {
            "wolnostojący": 1.0,
            "dobudowany": 0.9
        }
        return 200000 * mnoznik_aut[self.ilosc_aut] * mnoznik_rodzaju[self.rodzaj]


class Piwnica:
    def __init__(self, rodzaj: str, dom):
        self.rodzaj = rodzaj
        self.dlugosc = dom.dlugosc
        self.szerokosc = dom.szerokosc
        self.powierzchnia = self.szerokosc * self.dlugosc

    def koszt(self):
        mnoznik = {
            "użytkowa": 1.4,
            "magazynowa": 1.0
        }
        return mnoznik[self.rodzaj] * self.powierzchnia * 2000
