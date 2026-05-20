from src.dom import Dom, Garaz, Poddasze, Piwnica
from src.dzialka import Dzialka

cennik_materialow = {
    "beton": 250,
    "bloczek_fundamentowy": 5,
    "stal": 10,
    "strzemiono": 5
}


def koszt_wykopu(laczna_dlugosc, trudnosc, piwnica):
    if laczna_dlugosc <= 0 or trudnosc <= 0:
        raise ValueError("Podaj poprawne wartości liczbowe")
    if piwnica:
        glebokosc = 4
    else:
        glebokosc = 1.5
    wykop = laczna_dlugosc * ((0.6 + 2) * 0.5) * glebokosc
    koszt = round(wykop * trudnosc, 2) * 50
    return koszt


def koszt_fundamentow(dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica):
    if dlugosc <= 0 or szerokosc <= 0:
        raise ValueError("Podaj poprawne wartości liczbowe!")
    trudnosc = {
        "ziemia": 1.0,
        "glina": 1.2
    }
    if rodzaj_gleby not in trudnosc:
        raise ValueError("Podaj poprawny rodzaj gleby!")
    if piwnica:
        wysokosc_fundamentu = 4
    else:
        wysokosc_fundamentu = 1.5
    beton = koszt_materialow["beton"]
    bloczek = koszt_materialow["bloczek_fundamentowy"]
    stal = koszt_materialow["stal"]
    strzemiono = koszt_materialow["strzemiono"]
    laczna_dlugosc = (dlugosc * 2) + (szerokosc * 2)
    lawa_fundamentowa = round(laczna_dlugosc * 0.6 * 0.4 * beton, 2)
    sciana_fundamentowa = round((laczna_dlugosc / 0.38) * bloczek * (wysokosc_fundamentu/0.14), 2)
    wykop = koszt_wykopu(laczna_dlugosc, trudnosc[rodzaj_gleby], piwnica)
    zbrojenie = (4 * laczna_dlugosc * stal) + (((laczna_dlugosc / 0.2) * 1.8) * strzemiono)
    print("Ława fundamentowa: ", lawa_fundamentowa, "zł\nŚciana fundamentowa: ", sciana_fundamentowa,
          "zł\nKoszt wykopu: ", wykop, "zł\nZbrojenie: ", zbrojenie, "zł")
    koszt = lawa_fundamentowa + sciana_fundamentowa + wykop + zbrojenie
    return round(koszt, 2)


def pobierz_liczbe(tekst):
    while True:
        try:
            liczba = float(input(tekst))
            if liczba <= 0:
                print("Wartość musi być większa od 0!")
                continue
            return liczba
        except ValueError:
            print("To nie jest liczba!")


def pobierz_liczbe_calkowita(tekst):
    while True:
        try:
            liczba = int(input(tekst))
            if liczba <= 0:
                print("Wartość musi być większa od 0!")
                continue
            return liczba
        except ValueError:
            print("To nie jest liczba całkowita!")


def pobierz_boolean(tekst):
    while True:
        wartosc = input(tekst)
        if wartosc == "Tak" or wartosc == "tak":
            return True
        if wartosc == "Nie" or wartosc == "nie":
            return False
        else:
            print('Podaj "Tak" albo "Nie"!')


def pobierz_string(tekst, opcja1, opcja2):
    while True:
        wartosc = input(tekst)
        if wartosc == opcja1:
            return opcja1
        if wartosc == opcja2:
            return opcja2
        else:
            print(f'Podaj "{opcja1}" albo "{opcja2}" !')


def podaj_dane_garazu():
    while True:
        rodzaj = pobierz_string("Garaż ma być dobudowany czy wolnostojący: ", "dobudowany", "wolnostojący")
        ilosc_aut = pobierz_string("Podaj ile samochodów ma się mieścić w garażu: ", "1", "2")
        break
    return [rodzaj, ilosc_aut]


def podaj_dane_piwnicy():
    while True:
        rodzaj = pobierz_string("Czy piwnica ma być użytkowa czy magazynowa: ", "użytkowa", "magazynowa")
        break
    return [rodzaj]


def podaj_dane_poddasza():
    while True:
        rodzaj = pobierz_string("Czy poddasze ma być mieszkalne czy magazynowe: ", "mieszkalne", "magazynowe")
        break
    return [rodzaj]


def podaj_dane_drzew():
    while True:
        drzewa = pobierz_liczbe_calkowita("Podaj ile drzew należy wyciąć: ")
        break
    return drzewa


def podaj_dane_domu():
    while True:
        szerokosc = pobierz_liczbe("Podaj szerokość domu w metrach: ")
        dlugosc = pobierz_liczbe("Podaj długość domu w metrach: ")
        liczba_pieter = pobierz_liczbe("Podaj ile pięter ma mieć dom: ")
        ilosc_okien = pobierz_liczbe_calkowita("Podaj ile okien ma mieć dom: ")
        garaz = pobierz_boolean("Czy dom ma mieć garaż: ")
        piwnica = pobierz_boolean("Czy dom ma mieć piwnicę: ")
        poddasze = pobierz_boolean("Czy dom ma mieć poddasze: ")
        rodzaj = pobierz_string("Wybierz standard domu, standardowy lub luksusowy: ", "standardowy", "luksusowy")
        break
    return [szerokosc, dlugosc, liczba_pieter, ilosc_okien, garaz, piwnica, poddasze, rodzaj]


def podaj_dane_dzialki():
    while True:
        szerokosc = pobierz_liczbe("Podaj szerokość działki w metrach: ")
        dlugosc = pobierz_liczbe("Podaj długość działki w metrach: ")
        ogrodzenie = pobierz_boolean("Podaj czy działka ma ogrodzenie: ")
        uzbrojenie = pobierz_boolean("Podaj czy działka jest uzbrojona: ")
        drzewa = pobierz_boolean("Podaj czy konieczna jest wycinka drzew: ")
        rodzaj_gleby = pobierz_string("Podaj czy gleba działki to ziemia czy glina: ", "ziemia", "glina")
        break
    return [szerokosc, dlugosc, ogrodzenie, uzbrojenie, drzewa, rodzaj_gleby]


def podaj_dane_plotu():
    while True:
        rodzaj = pobierz_string("Podaj czy płot ma być zwykły czy drogi: ", "zwykły", "drogi")
        break
    return rodzaj


def czas_budowy(dom, dzialka, dane_plotu, ilosc_drzew, garaz, poddasze, piwnica):
    wynik = 0
    trudnosc = {
        "ziemia": 1.0,
        "glina": 1.2
    }
    mnoznik_plot = {
        "zwykły": 50,
        "drogi": 30
    }
    mnoznik_dom = {
        "standardowy": 1.0,
        "luksusowy": 1.5
    }
    mnoznik_garaz = {
        "dobudowany": 1.0,
        "wolnostojący": 1.5
    }
    mnoznik_poddasze = {
        "magazynowe": 1.0,
        "mieszkalne": 1.5
    }
    mnoznik_piwnica = {
        "magazynowa": 1.0,
        "użytkowa": 1.5
    }
    czas_dom = (dom.dlugosc * dom.szerokosc * dom.liczba_pieter * mnoznik_dom[dom.rodzaj])
    wynik += czas_dom
    czas_plot = (dzialka.dlugosc + dzialka.szerokosc) * 2 * trudnosc[dzialka.rodzaj_gleby] / mnoznik_plot[dane_plotu]
    wynik += czas_plot
    if dzialka.uzbrojenie is False:
        wynik += 60
    if dzialka.drzewa is True:
        wynik += ilosc_drzew / 4
    if dom.garaz is True:
        wynik += int(garaz.ilosc_aut) * 21 * mnoznik_garaz[garaz.rodzaj]
    if dom.poddasze is True:
        wynik += (poddasze.powierzchnia * mnoznik_poddasze[poddasze.rodzaj]) / 8
    if dom.piwnica is True:
        wynik += (piwnica.powierzchnia * mnoznik_piwnica[piwnica.rodzaj]) / 3
    return round(wynik * 1.05)


def uruchom():
    dom, dzialka, garaz, piwnica, poddasze = None, None, None, None, None
    dane_drzew = 0
    dane_plotu = "zwykły"
    while True:
        print("\n=========Menu=========")
        print("1. Podaj dane domu")
        print("2. Podaj dane działki")
        print("3. Pokaż koszty")
        print("4. Przewidywany czas wykonania")
        print("5. Zresetuj dane domu")
        print("6. Zresetuj dane działki")
        print("0. Wyjście")
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dane_domu = podaj_dane_domu()
            dom = Dom(dane_domu[0], dane_domu[1], dane_domu[2], dane_domu[3], dane_domu[4], dane_domu[5],
                      dane_domu[6], dane_domu[7])
            if dane_domu[4] is True:
                dane_garazu = podaj_dane_garazu()
                garaz = Garaz(dane_garazu[0], dane_garazu[1])
            if dane_domu[5] is True:
                dane_piwnicy = podaj_dane_piwnicy()
                piwnica = Piwnica(dane_piwnicy[0], dom)
            if dane_domu[6] is True:
                dane_poddasza = podaj_dane_poddasza()
                poddasze = Poddasze(dane_poddasza[0], dom)
        elif wybor == "2":
            dane_dzialki = podaj_dane_dzialki()
            dzialka = Dzialka(dane_dzialki[0], dane_dzialki[1], dane_dzialki[2], dane_dzialki[3],
                              dane_dzialki[4], dane_dzialki[5])
            if dane_dzialki[2] is False:
                dane_plotu = podaj_dane_plotu()
            if dane_dzialki[4] is True:
                dane_drzew = podaj_dane_drzew()
        elif wybor == "3":
            if dom is None:
                print("Najpierw podaj dane domu!")
                input("Aby wrócić do menu wciśnij Enter")
            elif dzialka is None:
                print("Najpierw podaj dane działki!")
                input("Aby wrócić do menu wciśnij Enter")
            else:
                print("koszt całkowity fundamentów: ", round(koszt_fundamentow(
                    dom.dlugosc, dom.szerokosc, cennik_materialow, dzialka.rodzaj_gleby, dom.piwnica), 2), "zł")
                print("Całkowity koszt przygotowania działki: ", dzialka.koszt_przygotowania_pod_budowe(
                    dane_plotu, dane_drzew), "zł\n")
                if dom.garaz is True:
                    print("Koszt budowy garażu: ", garaz.koszt(), "zł")
                if dom.piwnica is True:
                    print("Koszt budowy piwnicy: ", piwnica.koszt(), "zł")
                if dom.poddasze is True:
                    print("Koszt budowy poddasza: ", poddasze.koszt(), "zł")
                wyjdz = input("\nAby wrócić do menu wciśnij Enter\nAby wyjść z aplikacji podaj: 0\nInput: ")
                if wyjdz == "0":
                    break
                else:
                    continue
        elif wybor == "4":
            print(f"Przewidywany czas prac: {czas_budowy(
                dom, dzialka, dane_plotu, dane_drzew, garaz, poddasze, piwnica)} dni")
            wyjdz = input("\nAby wrócić do menu wciśnij Enter\nAby wyjść z aplikacji podaj: 0\nInput: ")
            if wyjdz == "0":
                break
            else:
                continue
        elif wybor == "5":
            dom.reset()
        elif wybor == "6":
            dzialka.reset()
        elif wybor == "0":
            print("Koniec programu")
            break
        else:
            print("Niepoprawna opcja")
