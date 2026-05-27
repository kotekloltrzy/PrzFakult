import pytest
from unittest.mock import patch
from src.menu import (
    pobierz_liczbe,
    pobierz_liczbe_calkowita,
    pobierz_boolean,
    pobierz_string,
    podaj_dane_domu,
    podaj_dane_garazu,
    podaj_dane_poddasza,
    podaj_dane_piwnicy,
    podaj_dane_dzialki,
    podaj_dane_drzew,
    podaj_dane_plotu,
    menu,
)


class TestPobierz:
    @pytest.mark.parametrize("wartosc", ["10", "15.5", "1"])
    def test_pobierz_liczbe_poprawnie(self, wartosc):
        with patch("builtins.input", return_value=wartosc):
            wynik = pobierz_liczbe("test", 0)
            assert wynik == float(wartosc)

    def test_pobierz_liczbe_niepoprawnie(self):
        with (
            patch("builtins.input", side_effect=["abc", "-5", "0", "10"]),
            patch("builtins.print") as mock_print,
        ):
            wynik = pobierz_liczbe("test", 0)
            assert wynik == 10
            mock_print.assert_any_call("To nie jest liczba!")
            mock_print.assert_any_call("Wartość musi być większa od 0!")

    def test_pobierz_liczbe_minimalna(self):
        with patch("builtins.input", return_value="0.1"):
            wynik = pobierz_liczbe("test", 0)
            assert wynik == 0.1

    @pytest.mark.parametrize(
        "wartosc, przewidywane",
        [
            ("Tak", True),
            ("tak", True),
            ("Nie", False),
            ("nie", False),
        ],
    )
    def test_pobierz_boolean_poprawnie(self, wartosc, przewidywane):
        with patch("builtins.input", return_value=wartosc):
            assert pobierz_boolean("test") is przewidywane

    def test_pobierz_boolean_niepoprawnie(self):
        with (
            patch("builtins.input", side_effect=["Jasne", "Nuh uh", "może", "tak"]),
            patch("builtins.print") as mock_print,
        ):
            wynik = pobierz_boolean("test")
            assert wynik is True
            mock_print.assert_any_call('Podaj "Tak" albo "Nie"!')

    def test_pobierz_string(self):
        with patch("builtins.input", side_effect=["zly", "standardowy"]):
            wynik = pobierz_string("test", "standardowy", "luksusowy")
            assert wynik == "standardowy"

    def test_pobierz_string_elif(self):
        with patch("builtins.input", side_effect=[12, "luksusowy"]):
            wynik = pobierz_string("test", "standardowy", "luksusowy")
            assert wynik == "luksusowy"

    def test_pobierz_string_niepoprawnie(self):
        with (
            patch("builtins.input", side_effect=[123, False, "", "123", "standardowy"]),
            patch("builtins.print") as mock_print,
        ):
            wynik = pobierz_string("test", "standardowy", "luksusowy")
            assert wynik == "standardowy"
            mock_print.assert_any_call(f'Podaj "standardowy" albo "luksusowy" !')

    @pytest.mark.parametrize("wartosc", ["1", "10", "100"])
    def test_pobierz_liczbe_calkowita_poprawnie(self, wartosc):
        with patch("builtins.input", return_value=wartosc):
            wynik = pobierz_liczbe_calkowita("test")
            assert wynik == int(wartosc)

    def test_pobierz_liczbe_calkowita_niepoprawnie(self):
        with (
            patch("builtins.input", side_effect=["-10", "0", "12.5", "10"]),
            patch("builtins.print") as mock_print,
        ):
            wynik = pobierz_liczbe_calkowita("test")
            assert wynik == 10
            mock_print.assert_any_call("To nie jest liczba całkowita!")
            mock_print.assert_any_call("Wartość musi być większa od 0!")

    def test_pobierz_liczbe_calkowita_minimalna(self):
        with patch("builtins.input", return_value="1"):
            wynik = pobierz_liczbe_calkowita("test")
            assert wynik == 1


class TestPodajDane:
    @patch("src.menu.pobierz_string")
    def test_podaj_dane_garazu_poprawnie(self, mock_input):
        mock_input.side_effect = ["dobudowany", "2"]
        wynik = podaj_dane_garazu()
        assert wynik == ["dobudowany", "2"]

    @patch("src.menu.pobierz_string")
    def test_podaj_dane_piwnicy_poprawnie(self, mock_input):
        mock_input.side_effect = ["użytkowa"]
        wynik = podaj_dane_piwnicy()
        assert wynik == ["użytkowa"]

    @patch("src.menu.pobierz_string")
    def test_podaj_dane_poddasza_poprawnie(self, mock_input):
        mock_input.side_effect = ["mieszkalne"]
        wynik = podaj_dane_poddasza()
        assert wynik == ["mieszkalne"]

    @patch("src.menu.pobierz_liczbe_calkowita")
    def test_podaj_dane_drzew_poprawnie(self, mock_input):
        mock_input.side_effect = [5]
        wynik = podaj_dane_drzew()
        assert wynik == 5

    @patch("builtins.input")
    def test_podaj_dane_domu_poprawnie(self, mock_input):
        mock_input.side_effect = [
            "10",
            "8",
            "2",
            "2",
            "10",
            "Nie",
            "Nie",
            "Nie",
            "standardowy",
        ]
        wynik = podaj_dane_domu()
        assert wynik == [10, 8, 2, 2, 10, False, False, False, "standardowy"]

    @patch("builtins.input")
    def test_podaj_dane_dzialki_poprawnie(self, mock_input):
        mock_input.side_effect = ["20", "30", "Tak", "Tak", "Nie", "ziemia"]
        wynik = podaj_dane_dzialki()
        assert wynik == [20, 30, True, True, False, "ziemia"]

    @patch("src.menu.pobierz_string")
    def test_podaj_dane_plotu_poprawnie(self, mock_input):
        mock_input.side_effect = ["drogi"]
        wynik = podaj_dane_plotu()
        assert wynik == "drogi"


class TestMenuGlownego:
    @patch("builtins.input")
    @patch("builtins.print")
    def test_menu_exit(self, mock_print, mock_input):
        mock_input.side_effect = ["0"]
        menu()
        mock_print.assert_any_call("Koniec programu")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_menu_niepoprawnie(self, mock_print, mock_input):
        mock_input.side_effect = ["999", "0"]
        menu()
        mock_print.assert_any_call("Niepoprawna opcja")
        mock_print.assert_any_call("Koniec programu")

    @pytest.mark.parametrize(
        "dane_domu, garaz_wywolania, piwnica_wywolania, poddasze_wywolania",
        [
            ([10, 8, 2, 2, 10, False, False, False, "standardowy"], 0, 0, 0),
            ([10, 8, 2, 2, 10, True, False, False, "standardowy"], 1, 0, 0),
            ([10, 8, 2, 2, 10, False, True, False, "standardowy"], 0, 1, 0),
            ([10, 8, 2, 2, 10, False, False, True, "standardowy"], 0, 0, 1),
            ([10, 8, 2, 2, 10, True, True, True, "standardowy"], 1, 1, 1),
        ],
    )
    @patch("src.menu.podaj_dane_garazu")
    @patch("src.menu.podaj_dane_piwnicy")
    @patch("src.menu.podaj_dane_poddasza")
    @patch("src.menu.podaj_dane_domu")
    @patch("src.menu.Dom")
    @patch("builtins.input")
    def test_menu_podaj_dane_domu(
        self,
        mock_input,
        mock_dom,
        mock_podaj_dane_domu,
        mock_podaj_dane_poddasza,
        mock_podaj_dane_piwnicy,
        mock_podaj_dane_garazu,
        dane_domu,
        garaz_wywolania,
        piwnica_wywolania,
        poddasze_wywolania,
    ):
        mock_input.side_effect = [
            "1",
            "0",
            "0",
            "0",
            "0",
        ]  # 1 by podać dane, 0 by wyjść
        mock_podaj_dane_domu.return_value = dane_domu
        mock_podaj_dane_garazu.return_value = ["dobudowany", "1"]
        mock_podaj_dane_piwnicy.return_value = ["użytkowa"]
        mock_podaj_dane_poddasza.return_value = ["mieszkalne"]
        menu()
        mock_podaj_dane_domu.assert_called_once()
        mock_dom.assert_called_once()
        assert mock_podaj_dane_garazu.call_count == garaz_wywolania
        assert mock_podaj_dane_piwnicy.call_count == piwnica_wywolania
        assert mock_podaj_dane_poddasza.call_count == poddasze_wywolania

    @pytest.mark.parametrize(
        "dane_dzialki, plot_wywolania, drzewa_wywolania",
        [
            ([30, 20, True, True, False, "ziemia"], 0, 0),
            ([30, 20, False, True, False, "glina"], 1, 0),
            ([30, 20, True, True, True, "ziemia"], 0, 1),
            ([30, 20, False, True, True, "glina"], 1, 1),
        ],
    )
    @patch("src.menu.podaj_dane_drzew")
    @patch("src.menu.podaj_dane_plotu")
    @patch("src.menu.podaj_dane_dzialki")
    @patch("src.menu.Dzialka")
    @patch("builtins.input")
    def test_menu_podaj_dane_dzialki(
        self,
        mock_input,
        mock_dzialka,
        mock_podaj_dane_dzialki,
        mock_podaj_dane_plotu,
        mock_podaj_dane_drzew,
        dane_dzialki,
        plot_wywolania,
        drzewa_wywolania,
    ):
        mock_input.side_effect = ["2", "0"]  # 2 by podać dane, 0 by wyjść
        mock_podaj_dane_dzialki.return_value = dane_dzialki
        menu()
        mock_podaj_dane_dzialki.assert_called_once()
        mock_dzialka.assert_called_once()
        assert mock_podaj_dane_plotu.call_count == plot_wywolania
        assert mock_podaj_dane_drzew.call_count == drzewa_wywolania

    @patch("src.menu.koszt_calkowity")
    @patch("src.menu.podaj_dane_dzialki")
    @patch("src.menu.podaj_dane_domu")
    @patch("builtins.input")
    def test_menu_koszt_wszystkiego(
        self, mock_input, mock_podaj_dane_domu, mock_podaj_dane_dzialki, mock_koszt
    ):
        mock_input.side_effect = ["1", "2", "3", "0", "0"]
        mock_podaj_dane_domu.return_value = [
            10,
            8,
            2,
            2,
            10,
            False,
            False,
            False,
            "standardowy",
        ]
        mock_podaj_dane_dzialki.return_value = [30, 20, True, True, False, "ziemia"]
        mock_koszt.return_value = 1000
        menu()
        mock_koszt.assert_called_once()

    @patch("builtins.input")
    @patch("builtins.print")
    def test_menu_koszt_brak_danych(self, mock_print, mock_input):
        mock_input.side_effect = ["3", "", "0"]
        menu()
        mock_print.assert_any_call("Najpierw podaj dane domu i działki!")

    @patch("builtins.input")
    @patch("builtins.print")
    @patch("src.menu.podaj_dane_domu")
    def test_menu_koszt_brak_dzialki(
        self, mock_podaj_dane_domu, mock_print, mock_input
    ):
        mock_input.side_effect = ["1", "3", "", "0"]
        mock_podaj_dane_domu.return_value = [
            10,
            8,
            2,
            2,
            10,
            False,
            False,
            False,
            "standardowy",
        ]
        menu()
        mock_print.assert_any_call("Najpierw podaj dane domu i działki!")

    @patch("builtins.input")
    @patch("builtins.print")
    @patch("src.menu.podaj_dane_dzialki")
    def test_menu_koszt_brak_domu(
        self, mock_podaj_dane_dzialki, mock_print, mock_input
    ):
        mock_input.side_effect = ["2", "3", "", "0"]
        mock_podaj_dane_dzialki.return_value = [20, 30, True, True, False, "ziemia"]
        menu()
        mock_print.assert_any_call("Najpierw podaj dane domu i działki!")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_menu_reset_domu_brak(self, mock_print, mock_input):
        mock_input.side_effect = ["5", "0"]
        menu()
        mock_print.assert_any_call("Brak danych domu do zresetowania")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_menu_reset_dzialki_brak(self, mock_print, mock_input):
        mock_input.side_effect = ["6", "0"]
        menu()
        mock_print.assert_any_call("Brak danych działki do zresetowania")

    @patch("builtins.input")
    @patch("src.menu.koszt_calkowity")
    @patch("src.menu.podaj_dane_domu")
    @patch("src.menu.podaj_dane_dzialki")
    def test_menu_koszty_wyjscie(
        self, mock_podaj_dane_dzialki, mock_podaj_dane_domu, mock_koszt, mock_input
    ):
        mock_input.side_effect = ["1", "2", "3", "0"]
        mock_podaj_dane_domu.return_value = [
            10,
            8,
            2,
            2,
            10,
            False,
            False,
            False,
            "standardowy",
        ]
        mock_podaj_dane_dzialki.return_value = [20, 30, True, True, False, "ziemia"]
        mock_koszt.return_value = 1000
        menu()
        mock_koszt.assert_called_once()

    @patch("builtins.input")
    @patch("src.menu.czas_budowy")
    @patch("src.menu.podaj_dane_domu")
    @patch("src.menu.podaj_dane_dzialki")
    def test_menu_czas_budowy(
        self, mock_podaj_dane_dzialki, mock_podaj_dane_domu, mock_czas, mock_input
    ):
        mock_input.side_effect = ["1", "2", "4", "0"]
        mock_podaj_dane_domu.return_value = [
            10,
            8,
            2,
            2,
            10,
            False,
            False,
            False,
            "standardowy",
        ]
        mock_podaj_dane_dzialki.return_value = [20, 30, True, True, False, "ziemia"]
        mock_czas.return_value = 120
        menu()
        mock_czas.assert_called_once()

    @patch("builtins.input")
    @patch("builtins.print")
    @patch("src.menu.podaj_dane_domu")
    @patch("src.menu.podaj_dane_dzialki")
    def test_menu_dom_po_resecie(
        self, mock_podaj_dane_dzialki, mock_podaj_dane_domu, mock_print, mock_input
    ):
        mock_input.side_effect = ["1", "5", "2", "3", "", "0"]
        mock_podaj_dane_domu.return_value = [
            10,
            8,
            2,
            2,
            10,
            False,
            False,
            False,
            "standardowy",
        ]
        mock_podaj_dane_dzialki.return_value = [20, 30, True, True, False, "ziemia"]
        menu()
        mock_print.assert_any_call("Najpierw podaj dane domu!")

    @patch("builtins.input")
    @patch("builtins.print")
    @patch("src.menu.podaj_dane_domu")
    @patch("src.menu.podaj_dane_dzialki")
    def test_menu_dzialka_po_resecie(
        self, mock_podaj_dane_dzialki, mock_podaj_dane_domu, mock_print, mock_input
    ):
        mock_input.side_effect = ["2", "6", "1", "3", "", "0"]
        mock_podaj_dane_domu.return_value = [
            10,
            8,
            2,
            2,
            10,
            False,
            False,
            False,
            "standardowy",
        ]
        mock_podaj_dane_dzialki.return_value = [20, 30, True, True, False, "ziemia"]
        menu()
        mock_print.assert_any_call("Najpierw podaj dane działki!")

    @pytest.mark.parametrize(
        "garaz, piwnica, poddasze, przewidywane",
        [
            (True, False, False, [("Koszt budowy garażu: ", 180000.0, "zł")]),
            (False, True, False, [("Koszt budowy piwnicy: ", 224000.0, "zł")]),
            (False, False, True, [("Koszt budowy poddasza: ", 120000, "zł")]),
            (
                True,
                True,
                True,
                [
                    ("Koszt budowy garażu: ", 180000.0, "zł"),
                    ("Koszt budowy piwnicy: ", 224000.0, "zł"),
                    ("Koszt budowy poddasza: ", 120000, "zł"),
                ],
            ),
        ],
    )
    @patch("builtins.input")
    @patch("builtins.print")
    @patch("src.menu.koszt_calkowity")
    @patch("src.menu.podaj_dane_domu")
    @patch("src.menu.podaj_dane_dzialki")
    @patch("src.menu.podaj_dane_garazu")
    @patch("src.menu.podaj_dane_piwnicy")
    @patch("src.menu.podaj_dane_poddasza")
    def test_menu_koszt_dodatkowe(
        self,
        mock_poddasze,
        mock_piwnica,
        mock_garaz,
        mock_dzialka,
        mock_dom,
        mock_koszt,
        mock_print,
        mock_input,
        garaz,
        piwnica,
        poddasze,
        przewidywane,
    ):
        mock_input.side_effect = ["1", "2", "3", "", "0"]
        mock_dom.return_value = [
            10,
            8,
            2,
            2,
            10,
            garaz,
            piwnica,
            poddasze,
            "standardowy",
        ]
        mock_dzialka.return_value = [20, 30, True, True, False, "ziemia"]
        mock_garaz.return_value = ["dobudowany", "1"]
        mock_piwnica.return_value = ["użytkowa"]
        mock_poddasze.return_value = ["mieszkalne"]
        mock_koszt.return_value = 1000
        menu()
        for i in przewidywane:
            mock_print.assert_any_call(*i)
