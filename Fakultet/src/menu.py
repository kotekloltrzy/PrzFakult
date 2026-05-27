from src.klasy import Dom, Garaz, Poddasze, Piwnica, Dzialka
from src.dzialania import (
    cennik_materialow,
    koszt_fundamentow,
    czas_budowy,
    koszt_domu,
    koszt_calkowity,
    koszt_instalacji,
)


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
        elif wartosc == opcja2:
            return opcja2
        else:
            print(f'Podaj "{opcja1}" albo "{opcja2}" !')


def podaj_dane_garazu():
    while True:
        rodzaj = pobierz_string(
            "Garaż ma być dobudowany czy wolnostojący: ", "dobudowany", "wolnostojący"
        )
        ilosc_aut = pobierz_string(
            "Podaj ile samochodów ma się mieścić w garażu: ", "1", "2"
        )
        break
    return [rodzaj, ilosc_aut]


def podaj_dane_piwnicy():
    while True:
        rodzaj = pobierz_string(
            "Czy piwnica ma być użytkowa czy magazynowa: ", "użytkowa", "magazynowa"
        )
        break
    return [rodzaj]


def podaj_dane_poddasza():
    while True:
        rodzaj = pobierz_string(
            "Czy poddasze ma być mieszkalne czy magazynowe: ",
            "mieszkalne",
            "magazynowe",
        )
        break
    return [rodzaj]


def podaj_dane_drzew():
    while True:
        drzewa = pobierz_liczbe_calkowita("Podaj ile drzew należy wyciąć: ")
        break
    return drzewa


def podaj_dane_domu():
    while True:
        dlugosc = pobierz_liczbe("Podaj długość domu w metrach: ")
        szerokosc = pobierz_liczbe("Podaj szerokość domu w metrach: ")
        liczba_pieter = pobierz_liczbe("Podaj ile pięter ma mieć dom: ")
        liczba_pokoi = pobierz_liczbe_calkowita(
            "Podaj ile pokoi ma być w domu (poza kuchnią i łązienką): "
        )
        ilosc_okien = pobierz_liczbe_calkowita("Podaj ile okien ma mieć dom: ")
        garaz = pobierz_boolean("Czy dom ma mieć garaż: ")
        piwnica = pobierz_boolean("Czy dom ma mieć piwnicę: ")
        poddasze = pobierz_boolean("Czy dom ma mieć poddasze: ")
        rodzaj = pobierz_string(
            "Wybierz standard domu, standardowy lub luksusowy: ",
            "standardowy",
            "luksusowy",
        )
        break
    return [
        dlugosc,
        szerokosc,
        liczba_pieter,
        liczba_pokoi,
        ilosc_okien,
        garaz,
        piwnica,
        poddasze,
        rodzaj,
    ]


def podaj_dane_dzialki():
    while True:
        dlugosc = pobierz_liczbe("Podaj długość działki w metrach: ")
        szerokosc = pobierz_liczbe("Podaj szerokość działki w metrach: ")
        ogrodzenie = pobierz_boolean("Podaj czy działka ma ogrodzenie: ")
        uzbrojenie = pobierz_boolean("Podaj czy działka jest uzbrojona: ")
        drzewa = pobierz_boolean("Podaj czy konieczna jest wycinka drzew: ")
        rodzaj_gleby = pobierz_string(
            "Podaj czy gleba działki to ziemia czy glina: ", "ziemia", "glina"
        )
        break
    return [dlugosc, szerokosc, ogrodzenie, uzbrojenie, drzewa, rodzaj_gleby]


def podaj_dane_plotu():
    while True:
        rodzaj = pobierz_string(
            "Podaj czy płot ma być zwykły czy drogi: ", "zwykły", "drogi"
        )
        break
    return rodzaj


def menu():
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
            dom = Dom(
                dane_domu[0],
                dane_domu[1],
                dane_domu[2],
                dane_domu[3],
                dane_domu[4],
                dane_domu[5],
                dane_domu[6],
                dane_domu[7],
                dane_domu[8],
            )
            if dane_domu[5] is True:
                dane_garazu = podaj_dane_garazu()
                garaz = Garaz(dane_garazu[0], dane_garazu[1])
            if dane_domu[6] is True:
                dane_piwnicy = podaj_dane_piwnicy()
                piwnica = Piwnica(dane_piwnicy[0], dom)
            if dane_domu[7] is True:
                dane_poddasza = podaj_dane_poddasza()
                poddasze = Poddasze(dane_poddasza[0], dom)
        elif wybor == "2":
            dane_dzialki = podaj_dane_dzialki()
            dzialka = Dzialka(
                dane_dzialki[0],
                dane_dzialki[1],
                dane_dzialki[2],
                dane_dzialki[3],
                dane_dzialki[4],
                dane_dzialki[5],
            )
            if dane_dzialki[2] is False:
                dane_plotu = podaj_dane_plotu()
            if dane_dzialki[4] is True:
                dane_drzew = podaj_dane_drzew()
        elif wybor == "3":
            if dom is None or dzialka is None:
                print("Najpierw podaj dane domu i działki!")
                input("Aby wrócić do menu wciśnij Enter")
                continue
            elif dom.state == "Brak danych":
                print("Najpierw podaj dane domu!")
                input("Aby wrócić do menu wciśnij Enter")
                continue
            elif dzialka.state == "Brak danych":
                print("Najpierw podaj dane działki!")
                input("Aby wrócić do menu wciśnij Enter")
                continue
            else:
                print(
                    "koszt całkowity fundamentów: ",
                    round(
                        koszt_fundamentow(
                            dom.dlugosc,
                            dom.szerokosc,
                            cennik_materialow,
                            dzialka.rodzaj_gleby,
                            dom.piwnica,
                        ),
                        2,
                    ),
                    "zł",
                )
                print(
                    "Całkowity koszt przygotowania działki: ",
                    dzialka.koszt_przygotowania_pod_budowe(dane_plotu, dane_drzew),
                    "zł\n",
                )
                print(
                    "Koszt gazobetonu na budowę domu: ",
                    koszt_domu(dom, cennik_materialow)[0],
                    "zł",
                )
                print(
                    "Koszt nadproży nad drzwi i okna: ",
                    koszt_domu(dom, cennik_materialow)[1],
                    "zł",
                )
                if dom.garaz is True:
                    print("Koszt budowy garażu: ", garaz.koszt(), "zł")
                if dom.piwnica is True:
                    print("Koszt budowy piwnicy: ", piwnica.koszt(), "zł")
                if dom.poddasze is True:
                    print("Koszt budowy poddasza: ", poddasze.koszt(), "zł")
                print(
                    "Koszt instalacji elektrycznej: ",
                    koszt_instalacji(dom, cennik_materialow)[0],
                    "zł",
                )
                print(
                    "Koszt instalacji hydraulicznej: ",
                    koszt_instalacji(dom, cennik_materialow)[1],
                    "zł",
                )
                print(
                    "Koszt instalacji ogrzewania: ",
                    koszt_instalacji(dom, cennik_materialow)[1],
                    "zł",
                )
                koszt_wszystkiego = koszt_calkowity(
                    dom, dzialka, dane_plotu, dane_drzew, garaz, piwnica, poddasze
                )
                print("\nKoszt całkowity prac budowlanych: ", koszt_wszystkiego, "zł")
                wyjdz = input(
                    "\nAby wrócić do menu wciśnij Enter\nAby wyjść z aplikacji podaj: 0\nInput: "
                )
                if wyjdz == "0":
                    break
                else:
                    continue
        elif wybor == "4":
            if dom is None or dzialka is None:
                print("Najpierw podaj dane domu i działki!")
                input("Aby wrócić do menu wciśnij Enter")
                continue
            elif dom.state == "Brak danych":
                print("Najpierw podaj dane domu!")
                input("Aby wrócić do menu wciśnij Enter")
                continue
            elif dzialka.state == "Brak danych":
                print("Najpierw podaj dane działki!")
                input("Aby wrócić do menu wciśnij Enter")
                continue
            print(f"Przewidywany czas prac: {czas_budowy(
                dom, dzialka, dane_plotu, dane_drzew, garaz, poddasze, piwnica)} dni")
            wyjdz = input(
                "\nAby wrócić do menu wciśnij Enter\nAby wyjść z aplikacji podaj: 0\nInput: "
            )
            if wyjdz == "0":
                break
            else:
                continue
        elif wybor == "5":
            if dom is not None:
                dom.reset()
            else:
                print("Brak danych domu do zresetowania")
        elif wybor == "6":
            if dzialka is not None:
                dzialka.reset()
            else:
                print("Brak danych działki do zresetowania")
        elif wybor == "0":
            print("Koniec programu")
            break
        else:
            print("Niepoprawna opcja")
