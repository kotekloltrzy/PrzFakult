cennik_materialow = {
    "beton": 250,  # cena za m3
    "bloczek_fundamentowy": 5,  # cena za sztukę
    "stal": 10,  # cena za kg
    "strzemiono": 5,  # cena za sztukę
    "nadproże": 100,  # cena za sztukę
    "gazobeton": 12,  # cena za sztukę
    "robocizna": 32,  # cena za 1h
    "blachodachówka": 65,  # cena za m2
    "dachówka": 90,  # cena za m2
    "hydraulika": 180,  # cena za m2
    "elektryka": 120,  # cena za m2
    "ogrzewanie": 220,  # cena za m2
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


def koszt_fundamentow(dlugosc, szerokosc, koszt_materialow,
                      rodzaj_gleby, piwnica):
    if dlugosc <= 0 or szerokosc <= 0:
        raise ValueError("Podaj poprawne wartości liczbowe!")
    trudnosc = {"ziemia": 1.0, "glina": 1.2}
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

    # dlugosc * szerokosc * wysokosc
    lawa_fundamentowa = round(laczna_dlugosc * 0.6 * 0.4 * beton, 2)

    # dlugosc / dlugosc bloczka * bloczek * wysokosc / wysokosc bloczka
    sciana_fundamentowa = round(
        (laczna_dlugosc / 0.38) * bloczek * (wysokosc_fundamentu / 0.14), 2
    )

    wykop = koszt_wykopu(laczna_dlugosc, trudnosc[rodzaj_gleby], piwnica)

    # 4 prety * dlugosc * koszt + dlugosc / 20cm odstepu * koszt
    zbrojenie = ((4 * laczna_dlugosc * stal) +
                 ((laczna_dlugosc / 0.2) * strzemiono))
    koszt = lawa_fundamentowa + sciana_fundamentowa + wykop + zbrojenie
    return round(koszt, 2)


def czas_budowy(
    dom, dzialka, dane_plotu, ilosc_drzew, garaz=None, poddasze=None, piwnica=None
):
    wynik = 0
    trudnosc = {"ziemia": 1.0, "glina": 1.2}
    mnoznik_plot = {"zwykły": 50, "drogi": 30}
    mnoznik_dom = {"standardowy": 1.0, "luksusowy": 1.5}
    mnoznik_garaz = {"dobudowany": 1.0, "wolnostojący": 1.5}
    mnoznik_poddasze = {"magazynowe": 1.0, "mieszkalne": 1.5}
    mnoznik_piwnica = {"magazynowa": 1.0, "użytkowa": 1.5}
    czas_dom = (
        dom.dlugosc
        * dom.szerokosc
        * dom.liczba_pieter
        * ((dom.liczba_pokoi + 2) * 0.33)
        * mnoznik_dom[dom.rodzaj]
    )
    wynik += czas_dom
    czas_plot = (
        (dzialka.dlugosc + dzialka.szerokosc)
        * 2
        * trudnosc[dzialka.rodzaj_gleby]
        / mnoznik_plot[dane_plotu]
    )
    wynik += czas_plot
    if dzialka.uzbrojenie is False:
        wynik += 60
    if dzialka.drzewa is True:
        wynik += ilosc_drzew / 4
    if dom.garaz is True and garaz is not None:
        wynik += int(garaz.ilosc_aut) * 21 * mnoznik_garaz[garaz.rodzaj]
    if dom.poddasze is True and garaz is not None:
        wynik += (poddasze.powierzchnia * mnoznik_poddasze[poddasze.rodzaj]) / 8
    if dom.piwnica is True and garaz is not None:
        wynik += (piwnica.powierzchnia * mnoznik_piwnica[piwnica.rodzaj]) / 3
    return round(wynik * 1.05)  # dodanie zapasu


def koszt_domu(
    dom,
    koszt_materialow,
):
    gazobeton = koszt_materialow["gazobeton"]
    nadproze = koszt_materialow["nadproże"]
    dlugosc_calkowita = (dom.szerokosc + dom.dlugosc) * 2

    # ilość bloczków na warstwe = dlugosc / dlugosc bloczka
    bloczek_warstwa = dlugosc_calkowita / 0.59

    # ilość bloczków na piętro = warstwa * 10 warstw
    bloczek_pietro = bloczek_warstwa * 10

    # ilość bloczków na dom = pietro * liczba pięter
    bloczek_dom = bloczek_pietro * dom.liczba_pieter

    # koszt nadproży = ilosc okien * koszt nadproża + ilosc drzwi (jedne drzwi na pokój + drzwi wejściowe) * koszt
    cena_nadproza = (dom.ilosc_okien * nadproze) + ((dom.liczba_pokoi + 3) * nadproze)

    # wyrównanie ilości bloczków za okna
    bloczek_dom -= dom.ilosc_okien * 24

    # wyrównanie ilości bloczków za ściany między pokojami
    bloczek_sciany = (dom.liczba_pokoi + 2) * (bloczek_warstwa / 4)
    bloczek_dom += bloczek_sciany

    # cena bloczków = całkowita ilość bloczków * cena za bloczek
    cena_bloczki = bloczek_dom * gazobeton

    return round(cena_bloczki, 2), round(cena_nadproza, 2)


def koszt_dachu(dom, koszt_materialow, poddasze=None):
    blacha = koszt_materialow["blachodachówka"]
    dachowka = koszt_materialow["dachówka"]
    if poddasze is None:
        wysokosc = 1.5
    elif poddasze == "mieszkalne":
        wysokosc = 2.5
    else:
        wysokosc = 2
    przeciw = (
        wysokosc**2 + (dom.szerokosc / 2) ** 2
    ) ** 0.5  # przeciwprostokątna dachu
    powierzchnia = 2 * (przeciw * dom.dlugosc)
    if dom.rodzaj == "standardowy":
        wynik = powierzchnia * blacha
    else:
        wynik = powierzchnia * dachowka
    return round(wynik, 2)


def koszt_robocizny(
    dom, dzialka, koszt, dane_plotu, ilosc_drzew, garaz, poddasze, piwnica
):
    czas = czas_budowy(dom, dzialka, dane_plotu, ilosc_drzew, garaz, poddasze, piwnica)
    return czas * koszt["robocizna"] * 10  # ilość dni * koszt na godzine * 10h dziennie


def koszt_instalacji(dom, koszt):
    elektryka = koszt["elektryka"]
    hydraulika = koszt["hydraulika"]
    ogrzewanie = koszt["ogrzewanie"]
    mnoznik_standardu = {"standardowy": 1.0, "luksusowy": 1.5}
    powierzchnia = dom.dlugosc * dom.szerokosc
    koszt_elektryka = (
        elektryka * powierzchnia * mnoznik_standardu[dom.rodzaj] * dom.liczba_pieter
    )
    koszt_hydraulika = (
        hydraulika * powierzchnia * mnoznik_standardu[dom.rodzaj] * dom.liczba_pieter
    )
    koszt_ogrzewanie = (
        ogrzewanie * powierzchnia * mnoznik_standardu[dom.rodzaj] * dom.liczba_pieter
    )
    return (
        round(koszt_ogrzewanie, 2),
        round(koszt_hydraulika, 2),
        round(koszt_elektryka, 2),
    )


def koszt_calkowity(
    dom, dzialka, dane_plotu, dane_drzew, garaz=None, piwnica=None, poddasze=None
):
    wynik = 0
    wynik += koszt_fundamentow(
        dom.dlugosc, dom.szerokosc, cennik_materialow, dzialka.rodzaj_gleby, dom.piwnica
    )
    wynik += dzialka.koszt_przygotowania_pod_budowe(dane_plotu, dane_drzew)
    wynik += koszt_domu(dom, cennik_materialow)[0]
    wynik += koszt_domu(dom, cennik_materialow)[1]
    wynik += koszt_dachu(dom, cennik_materialow)
    if dom.garaz:
        wynik += garaz.koszt()
    if dom.piwnica:
        wynik += piwnica.koszt()
    if dom.poddasze:
        wynik += poddasze.koszt()
    wynik += koszt_robocizny(
        dom,
        dzialka,
        cennik_materialow,
        dane_plotu,
        dane_drzew,
        garaz,
        poddasze,
        piwnica,
    )
    wynik += (
        koszt_instalacji(dom, cennik_materialow)[0]
        + koszt_instalacji(dom, cennik_materialow)[1]
        + koszt_instalacji(dom, cennik_materialow)[2]
    )
    return wynik
