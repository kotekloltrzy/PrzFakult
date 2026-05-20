import pytest
from src.dzialka import Dzialka


# określenie danych działki
@pytest.fixture
def dzialka():
    return Dzialka(30, 40, False, False, True, "ziemia")


# test resetowania danych działki
def test_dzialka_reset(dzialka):
    dzialka.reset()
    assert (dzialka.szerokosc is None and dzialka.dlugosc is None and dzialka.ogrodzenie is None
            and dzialka.uzbrojenie is None and dzialka.drzewa is None and dzialka.rodzaj_gleby is None)


# określenie danych ogrodzenia z parametryzacją
@pytest.mark.parametrize(
    "rodzaj, przewidywanie",
    [
        ("zwykły", 12600),
        ("drogi", 21000)
    ]

)
# test kosztu ogrodzenia
def test_dzialka_koszt_ogrodzenia(dzialka, rodzaj, przewidywanie):
    assert dzialka.koszt_ogrodzenia(rodzaj) == przewidywanie


# określenie danych działki z parametryzacją
@pytest.mark.parametrize(
    "szerokosc, dlugosc, ogrodzenie, uzbrojenie, drzewa, rodzaj_gleby, standard_plotu, ilosc_drzew, przewidywanie",
    [
        (30, 40, False, False, True, "glina", "zwykły", 5, 28400),
        (20, 30, True, True, False, "ziemia", "drogi", 0, 0)
    ]
)
# test kosztu przygotowania pod budowę
def test_dzialka_koszt_przygotowania_pod_budowe(szerokosc, dlugosc, ogrodzenie, uzbrojenie, drzewa,
                                                rodzaj_gleby, standard_plotu, ilosc_drzew, przewidywanie):
    dzialka = Dzialka(szerokosc, dlugosc, ogrodzenie, uzbrojenie, drzewa, rodzaj_gleby)
    assert dzialka.koszt_przygotowania_pod_budowe(standard_plotu, ilosc_drzew) == przewidywanie
