import pytest
from unittest.mock import Mock
from src.dzialania import (
    koszt_wykopu,
    koszt_fundamentow,
    cennik_materialow,
    czas_budowy,
    koszt_domu,
    koszt_dachu,
    koszt_calkowity,
    koszt_instalacji,
    koszt_robocizny,
)
from src.klasy import Dom, Garaz, Piwnica, Poddasze, Dzialka


class TestKosztWykopu:
    @pytest.mark.parametrize(
        "dlugosc, trudnosc, piwnica, przewidywane",
        [(100, 1.0, True, 26000), (100, 1.0, False, 9750), (50, 1.2, False, 5850)],
    )
    def test_koszt_wykopu_poprawnie(self, dlugosc, trudnosc, piwnica, przewidywane):
        assert koszt_wykopu(dlugosc, trudnosc, piwnica) == przewidywane

    @pytest.mark.parametrize(
        "dlugosc, trudnosc, piwnica",
        [
            (0, 1.0, True),
            (100, -5, False),
        ],
    )
    def test_koszt_wykopu_niepoprawnie(self, dlugosc, trudnosc, piwnica):
        with pytest.raises(ValueError):
            koszt_wykopu(dlugosc, trudnosc, piwnica)

    def test_koszt_wykopu_minimalne_wartosci(self):
        wynik = koszt_wykopu(0.1, 0.1, False)
        assert wynik > 0


class TestKosztFundamentow:
    @pytest.mark.parametrize(
        "dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica, przewidywane",
        [
            (7.5, 5, cennik_materialow, "ziemia", True, 19023.5),
            (7.5, 5, cennik_materialow, "ziemia", False, 9086.94),
            (10, 8, cennik_materialow, "glina", True, 29265.83),
            (10, 8, cennik_materialow, "glina", False, 13787.19),
        ],
    )
    def test_koszt_fundamentow_poprawnie(
        self, dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica, przewidywane
    ):
        assert (
            koszt_fundamentow(
                dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica
            )
            == przewidywane
        )

    @pytest.mark.parametrize(
        "dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica",
        [
            (-1, 5, cennik_materialow, "ziemia", True),
            (7.5, 0, cennik_materialow, "ziemia", False),
            (10, 8, cennik_materialow, "woda", True),
        ],
    )
    def test_koszt_fundamentow_niepoprawnie(
        self, dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica
    ):
        with pytest.raises(ValueError):
            koszt_fundamentow(
                dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica
            )

    def test_koszt_fundamentow_minimalne_wartosci(self):
        wynik = koszt_fundamentow(0.1, 0.1, cennik_materialow, "ziemia", False)
        assert wynik > 0


class TestCzasBudowy:
    def test_czas_budowy_krotki(self):
        dom = Dom(6, 7, 1, 2, 5, False, False, False, "standardowy")
        dzialka = Dzialka(20, 30, True, True, False, "ziemia")
        garaz = Garaz("dobudowany", "1")
        poddasze = Poddasze("mieszkalne", dom)
        piwnica = Piwnica("użytkowa", dom)
        wynik = czas_budowy(dom, dzialka, "zwykły", 8, garaz, poddasze, piwnica)
        assert isinstance(wynik, int)
        assert wynik == 60

    def test_czas_budowy_dlugi(self):
        dom = Dom(10, 8, 3, 15, 10, True, True, True, "luksusowy")
        dzialka = Dzialka(20, 30, False, False, True, "glina")
        garaz = Garaz("wolnostojący", "2")
        poddasze = Poddasze("mieszkalne", dom)
        piwnica = Piwnica("użytkowa", dom)
        wynik = czas_budowy(dom, dzialka, "zwykły", 8, garaz, poddasze, piwnica)
        assert isinstance(wynik, int)
        assert wynik == 2312

    def test_czas_budowy_minimalny(self):
        dom = Dom(1, 1, 1, 1, 1, False, False, False, "standardowy")
        dzialka = Dzialka(1, 1, True, True, False, "ziemia")
        wynik = czas_budowy(dom, dzialka, "zwykły", 0)
        assert wynik > 0


class TestKosztDomu:
    @pytest.mark.parametrize(
        "dlugosc, szerokosc, liczba_pieter, liczba_pokoi, ilosc_okien, garaz, piwnica, poddasze,"
        " rodzaj, przewidywane",
        [
            (6, 7, 2, 3, 6, False, False, True, "standardowy", (9509.29, 1200)),
            (10, 8, 1, 4, 7, True, True, False, "luksusowy", (6404.34, 1400)),
        ],
    )
    def test_koszt_domu(
        self,
        dlugosc,
        szerokosc,
        liczba_pieter,
        liczba_pokoi,
        ilosc_okien,
        garaz,
        piwnica,
        poddasze,
        rodzaj,
        przewidywane,
    ):
        dom = Dom(
            dlugosc,
            szerokosc,
            liczba_pieter,
            liczba_pokoi,
            ilosc_okien,
            garaz,
            piwnica,
            poddasze,
            rodzaj,
        )
        assert koszt_domu(dom, cennik_materialow) == przewidywane

    @pytest.mark.parametrize(
        "dlugosc, szerokosc, liczba_pieter, liczba_pokoi, ilosc_okien, garaz, piwnica, poddasze,"
        " rodzaj, rodzaj_poddasza, przewidywane",
        [
            (6, 7, 2, 3, 6, False, False, False, "standardowy", None, 2970.15),
            (10, 8, 1, 4, 7, True, False, False, "standardowy", None, 5553.6),
            (6, 7, 2, 3, 6, True, True, True, "luksusowy", "magazynowe", 4353.62),
            (10, 8, 1, 4, 7, False, True, True, "luksusowy", "mieszkalne", 8490.58),
        ],
    )
    def test_koszt_dachu(
        self,
        dlugosc,
        szerokosc,
        liczba_pieter,
        liczba_pokoi,
        ilosc_okien,
        garaz,
        piwnica,
        poddasze,
        rodzaj,
        przewidywane,
        rodzaj_poddasza,
    ):
        dom = Dom(
            dlugosc,
            szerokosc,
            liczba_pieter,
            liczba_pokoi,
            ilosc_okien,
            garaz,
            piwnica,
            poddasze,
            rodzaj,
        )
        assert koszt_dachu(dom, cennik_materialow, rodzaj_poddasza) == przewidywane

    @pytest.mark.parametrize(
        "dom_dane, dzialka_dane, plot_dane, drzewa_dane, garaz, piwnica, poddasze",
        [
            (
                (6, 7, 2, 3, 6, False, False, False, "standardowy"),
                (20, 30, True, True, False, "ziemia"),
                "zwykły",
                0,
                None,
                None,
                None,
            ),
            (
                (6, 7, 2, 3, 6, True, False, False, "standardowy"),
                (20, 30, True, True, False, "glina"),
                "zwykły",
                0,
                Garaz("dobudowany", "1"),
                None,
                None,
            ),
            (
                (6, 7, 2, 3, 6, False, True, False, "luksusowy"),
                (20, 30, True, True, False, "ziemia"),
                "drogi",
                0,
                None,
                Piwnica(
                    "użytkowa", Dom(6, 7, 2, 3, 6, False, False, False, "luksusowy")
                ),
                None,
            ),
            (
                (6, 7, 2, 3, 6, False, False, True, "standardowy"),
                (20, 30, True, True, False, "glina"),
                "drogi",
                0,
                None,
                None,
                Poddasze(
                    "mieszkalne", Dom(6, 7, 2, 3, 6, False, False, False, "standardowy")
                ),
            ),
            (
                (6, 7, 2, 3, 6, True, True, True, "standardowy"),
                (20, 30, True, True, False, "ziemia"),
                "zwykły",
                0,
                Garaz("wolnostojący", "2"),
                Piwnica(
                    "użytkowa", Dom(6, 7, 2, 3, 6, False, False, False, "luksusowy")
                ),
                Poddasze(
                    "mieszkalne", Dom(6, 7, 2, 3, 6, False, False, False, "standardowy")
                ),
            ),
        ],
    )
    def test_koszt_calkowity(
        self, dom_dane, dzialka_dane, plot_dane, drzewa_dane, garaz, piwnica, poddasze
    ):
        dom = Dom(*dom_dane)
        dzialka = Dzialka(*dzialka_dane)
        if garaz is not None:
            garaz.koszt = Mock(return_value=1000)
        if piwnica is not None:
            piwnica.koszt = Mock(return_value=2000)
        if poddasze is not None:
            poddasze.koszt = Mock(return_value=3000)
        wynik = koszt_calkowity(
            dom, dzialka, plot_dane, drzewa_dane, garaz, piwnica, poddasze
        )
        assert isinstance(wynik, (int, float))
        assert wynik > 0
        if garaz is not None:
            garaz.koszt.assert_called_once()
        if piwnica is not None:
            piwnica.koszt.assert_called_once()
        if poddasze is not None:
            poddasze.koszt.assert_called_once()

    def test_koszt_domu_minimalny(self):
        dom = Dom(1, 1, 1, 1, 1, False, False, False, "standardowy")
        koszt_bloczkow, koszt_nadprozy = koszt_domu(dom, cennik_materialow)
        assert koszt_bloczkow > 0
        assert koszt_nadprozy > 0

    @pytest.mark.parametrize(
        "dom_dane, dzialka_dane, plot_dane, drzewa_dane, garaz, poddasze, piwnica, przewidywanie",
        [
            (
                (6, 7, 1, 2, 5, False, False, False, "standardowy"),
                (20, 30, True, True, False, "ziemia"),
                "zwykły",
                0,
                None,
                None,
                None,
                19200,
            ),
            (
                (10, 8, 3, 15, 10, True, True, True, "luksusowy"),
                (20, 30, False, False, True, "glina"),
                "drogi",
                8,
                Garaz("wolnostojący", "2"),
                Poddasze(
                    "mieszkalne", Dom(10, 8, 3, 15, 10, True, True, True, "luksusowy")
                ),
                Piwnica(
                    "użytkowa", Dom(10, 8, 3, 15, 10, True, True, True, "luksusowy")
                ),
                740480,
            ),
        ],
    )
    def test_koszt_robocizny(
        self,
        dom_dane,
        dzialka_dane,
        plot_dane,
        drzewa_dane,
        garaz,
        poddasze,
        piwnica,
        przewidywanie,
    ):
        dom = Dom(*dom_dane)
        dzialka = Dzialka(*dzialka_dane)
        wynik = koszt_robocizny(
            dom,
            dzialka,
            cennik_materialow,
            plot_dane,
            drzewa_dane,
            garaz,
            poddasze,
            piwnica,
        )
        assert wynik == przewidywanie

    @pytest.mark.parametrize(
        "dom_dane, przewidywane",
        [
            (
                (10, 8, 1, 4, 7, False, False, False, "standardowy"),
                (17600.0, 14400.0, 9600.0),
            ),
            (
                (10, 8, 1, 4, 7, True, True, True, "luksusowy"),
                (26400.0, 21600.0, 14400.0),
            ),
        ],
    )
    def test_koszt_instalacji(self, dom_dane, przewidywane):
        dom = Dom(*dom_dane)
        wynik = koszt_instalacji(dom, cennik_materialow)
        assert wynik == przewidywane


class TestKosztDzialki:
    def test_koszt_dzialka_ogrodzenie_gdy_ogrodzenie(self):
        dzialka = Dzialka(20, 30, True, True, False, "ziemia")
        assert dzialka.koszt_ogrodzenia("zwykły") == 0

    def test_koszt_dzialka_przygotowanie_bez_drzew(self):
        dzialka = Dzialka(20, 20, False, True, False, "ziemia")
        wynik = dzialka.koszt_przygotowania_pod_budowe("zwykły", 0)
        assert wynik > 0
