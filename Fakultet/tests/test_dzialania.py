import pytest
from unittest.mock import patch
from src.dzialania import (pobierz_liczbe, pobierz_liczbe_calkowita, pobierz_boolean, pobierz_string,
                           koszt_wykopu, koszt_fundamentow, cennik_materialow, czas_budowy, podaj_dane_plotu,
                           podaj_dane_drzew, podaj_dane_garazu, podaj_dane_poddasza, podaj_dane_piwnicy,
                           podaj_dane_dzialki, podaj_dane_domu, uruchom)


from src.dom import Dom, Garaz, Piwnica, Poddasze
from src.dzialka import Dzialka


class TestPobierz:
    @pytest.mark.parametrize(
        "wartosc",
        ["10", "15.5", "1"]
    )
    def test_pobierz_liczbe_poprawnie(self, wartosc):
        with patch("builtins.input", return_value=wartosc):
            wynik = pobierz_liczbe("test")
            assert wynik == float(wartosc)

    def test_pobierz_liczbe_niepoprawnie(self):
        with (
            patch(
                "builtins.input",
                side_effect=["abc", "-5", "0", "10"]
            ),
            patch("builtins.print") as mock_print
        ):
            wynik = pobierz_liczbe("test")
            assert wynik == 10
            mock_print.assert_any_call("To nie jest liczba!")
            mock_print.assert_any_call("Wartość musi być większa od 0!")

    @pytest.mark.parametrize(
        "wartosc, przewidywane",
        [
            ("Tak", True),
            ("tak", True),
            ("Nie", False),
            ("nie", False),
        ]
    )
    def test_pobierz_boolean_poprawnie(self, wartosc, przewidywane):
        with patch("builtins.input", return_value=wartosc):
            assert pobierz_boolean("test") is przewidywane

    def test_pobierz_boolean_niepoprawnie(self):
        with (
            patch(
                "builtins.input",
                side_effect=["Jasne", "Nuh uh", "może", "tak"]
            ),
            patch("builtins.print") as mock_print
        ):
            wynik = pobierz_boolean("test")
            assert wynik is True
            mock_print.assert_any_call('Podaj "Tak" albo "Nie"!')

    def test_pobierz_string_poprawnie(self):
        with patch(
            "builtins.input",
            side_effect=["zly", "standardowy"]
        ):
            wynik = pobierz_string(
                "test",
                "standardowy",
                "luksusowy"
            )
            assert wynik == "standardowy"

    def test_pobierz_string_niepoprawnie(self):
        with (
            patch(
                "builtins.input",
                side_effect=[123, False, "", "123", "standardowy"]
            ),
            patch("builtins.print") as mock_print
        ):
            wynik = pobierz_string("test", "standardowy", "luksusowy")
            assert wynik == "standardowy"
            mock_print.assert_any_call(f'Podaj "standardowy" albo "luksusowy" !')

    @pytest.mark.parametrize(
        "wartosc",
        ["1", "10", "100"]
    )
    def test_pobierz_liczbe_calkowita_poprawnie(self, wartosc):
        with patch("builtins.input", return_value=wartosc):
            wynik = pobierz_liczbe_calkowita("test")
            assert wynik == int(wartosc)

    def test_pobierz_liczbe_calkowita_niepoprawnie(self):
        with (
            patch(
                "builtins.input",
                side_effect=["-10", "0", "12.5", "10"]
            ),
            patch("builtins.print") as mock_print
        ):
            wynik = pobierz_liczbe_calkowita("test")
            assert wynik == 10
            mock_print.assert_any_call("To nie jest liczba całkowita!")
            mock_print.assert_any_call("Wartość musi być większa od 0!")


class TestKosztWykopu:
    @pytest.mark.parametrize(
        "dlugosc, trudnosc, piwnica, przewidywane",
        [
            (100, 1.0, True, 26000),
            (100, 1.0, False, 9750),
            (50, 1.2, False, 5850)
        ]
    )
    def test_koszt_wykopu_poprawnie(self, dlugosc, trudnosc, piwnica, przewidywane):
        assert koszt_wykopu(dlugosc, trudnosc, piwnica) == przewidywane

    @pytest.mark.parametrize(
        "dlugosc, trudnosc, piwnica",
        [
            (0, 1.0, True),
            (100, -5, False),
        ]
    )
    def test_koszt_wykopu_niepoprawnie(self, dlugosc, trudnosc, piwnica):
        with pytest.raises(ValueError):
            koszt_wykopu(dlugosc, trudnosc, piwnica)


class TestKosztFundamentow:
    @pytest.mark.parametrize(
        "dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica, przewidywane",
        [
            (7.5, 5, cennik_materialow, "ziemia", True, 19523.5),
            (7.5, 5, cennik_materialow, "ziemia", False, 9586.94),
            (10, 8, cennik_materialow, "glina", True, 29985.83),
            (10, 8, cennik_materialow, "glina", False, 14507.19)
        ]
    )
    def test_koszt_fundamentow_poprawnie(self, dlugosc, szerokosc,
                                         koszt_materialow, rodzaj_gleby, piwnica, przewidywane):
        assert koszt_fundamentow(dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica) == przewidywane

    @pytest.mark.parametrize(
        "dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica",
        [
            (-1, 5, cennik_materialow, "ziemia", True),
            (7.5, 0, cennik_materialow, "ziemia", False),
            (10, 8, cennik_materialow, "woda", True)
        ]
    )
    def test_koszt_fundamentow_niepoprawnie(self, dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica):
        with pytest.raises(ValueError):
            koszt_fundamentow(dlugosc, szerokosc, koszt_materialow, rodzaj_gleby, piwnica)


class TestPodajDane:
    @patch("src.dzialania.pobierz_string")
    def test_podaj_dane_garazu_poprawnie(self, mock_input):
        mock_input.side_effect = ["dobudowany", "2"]
        wynik = podaj_dane_garazu()
        assert wynik == ["dobudowany", "2"]

    @patch("src.dzialania.pobierz_string")
    def test_podaj_dane_piwnicy_poprawnie(self, mock_input):
        mock_input.side_effect = ["użytkowa"]
        wynik = podaj_dane_piwnicy()
        assert wynik == ["użytkowa"]

    @patch("src.dzialania.pobierz_string")
    def test_podaj_dane_poddasza_poprawnie(self, mock_input):
        mock_input.side_effect = ["mieszkalne"]
        wynik = podaj_dane_poddasza()
        assert wynik == ["mieszkalne"]

    @patch("src.dzialania.pobierz_liczbe_calkowita")
    def test_podaj_dane_drzew_poprawnie(self, mock_input):
        mock_input.side_effect = [5]
        wynik = podaj_dane_drzew()
        assert wynik == 5

    @patch("builtins.input")
    def test_podaj_dane_domu_poprawnie(self, mock_input):
        mock_input.side_effect = ["10", "8", "2", "10", "Nie", "Nie", "Nie", "standardowy"]
        wynik = podaj_dane_domu()
        assert wynik == [10, 8, 2, 10, False, False, False, "standardowy"]

    @patch("builtins.input")
    def test_podaj_dane_dzialki_poprawnie(self, mock_input):
        mock_input.side_effect = ["20", "30", "Tak", "Tak", "Nie", "ziemia"]
        wynik = podaj_dane_dzialki()
        assert wynik == [20, 30, True, True, False, "ziemia"]

    @patch("src.dzialania.pobierz_string")
    def test_podaj_dane_plotu_poprawnie(self, mock_input):
        mock_input.side_effect = ["drogi"]
        wynik = podaj_dane_plotu()
        assert wynik == "drogi"


class TestCzasBudowy:
    def test_czas_budowy_krotki(self):
        dom = Dom(10, 8, 1, 10, False, False, False, "standardowy")
        dzialka = Dzialka(20, 30, True, True, False, "ziemia")
        garaz = Garaz("dobudowany", "1")
        poddasze = Poddasze("mieszkalne", dom)
        piwnica = Piwnica("użytkowa", dom)
        wynik = czas_budowy(dom, dzialka, "zwykły", 8, garaz, poddasze, piwnica)
        assert isinstance(wynik, int)
        assert wynik == 86

    def test_czas_budowy_dlugi(self):
        dom = Dom(10, 8, 3, 10, True, True, True, "luksusowy")
        dzialka = Dzialka(20, 30, False, False, True, "glina")
        garaz = Garaz("wolnostojący", "2")
        poddasze = Poddasze("mieszkalne", dom)
        piwnica = Piwnica("użytkowa", dom)
        wynik = czas_budowy(dom, dzialka, "zwykły", 8, garaz, poddasze, piwnica)
        assert isinstance(wynik, int)
        assert wynik == 570


class TestDzialania:
    @patch("builtins.input")
    @patch("builtins.print")
    def test_dzialania_exit(self, mock_print, mock_input):
        mock_input.side_effect = ["0"]
        uruchom()
        mock_print.assert_any_call("Koniec programu")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_dzialania_niepoprawnie(self, mock_print, mock_input):
        mock_input.side_effect = ["999", "0"]
        uruchom()
        mock_print.assert_any_call("Niepoprawna opcja")
        mock_print.assert_any_call("Koniec programu")

    @patch("src.dzialania.podaj_dane_domu")
    @patch("src.dzialania.Dom")
    @patch("builtins.input")
    def test_dzialania_podaj_dane_domu(self, mock_input, mock_dom, mock_podaj_dane_domu):
        mock_input.side_effect = ["1", "0"]
        mock_podaj_dane_domu.return_value = [10, 8, 2, 10, False, False, False, "standardowy"]
        uruchom()
        mock_podaj_dane_domu.assert_called_once()
        mock_dom.assert_called_once()
