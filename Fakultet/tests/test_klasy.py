import pytest
from src.klasy import Dom, Poddasze, Garaz, Piwnica, Dzialka


# określenie danych domu
@pytest.fixture
def dom():
    return Dom(9.5, 7.5, 2, 4, 10, True, True, True, "standardowy")


# test resetowania danych domu
def test_reset(dom):
    dom.reset()
    assert (
        dom.szerokosc is None
        and dom.dlugosc is None
        and dom.liczba_pieter is None
        and dom.ilosc_okien is None
        and dom.garaz is None
        and dom.piwnica is None
        and dom.poddasze is None
        and dom.rodzaj is None
        and dom.state == "Brak danych"
    )


# określenie danych poddasza z parametryzacją
@pytest.mark.parametrize(
    "rodzaj, przewidywane", [("mieszkalne", 106875), ("magazynowe", 26718.75)]
)
# test kosztu poddasza
def test_poddasze_koszt(dom, rodzaj, przewidywane):
    poddasze = Poddasze(rodzaj, dom)
    assert poddasze.koszt() == przewidywane


# określenie danych piwnicy z parametryzacją
@pytest.mark.parametrize(
    "rodzaj, przewidywane", [("użytkowa", 199500), ("magazynowa", 142500)]
)
# test kosztu piwnicy
def test_piwnica_koszt(dom, rodzaj, przewidywane):
    piwnica = Piwnica(rodzaj, dom)
    assert piwnica.koszt() == przewidywane


# określenie danych garażu z parametryzacją
@pytest.mark.parametrize(
    "rodzaj, ilosc_aut, przewidywane",
    [("wolnostojący", "2", 340000), ("dobudowany", "1", 180000)],
)
# test kosztu garażu
def test_garaz_koszt(rodzaj, ilosc_aut, przewidywane):
    garaz = Garaz(rodzaj, ilosc_aut)
    assert garaz.koszt() == przewidywane


# określenie danych działki
@pytest.fixture
def dzialka():
    return Dzialka(30, 40, False, False, True, "ziemia")


# test resetowania danych działki
def test_dzialka_reset(dzialka):
    dzialka.reset()
    assert (
        dzialka.szerokosc is None
        and dzialka.dlugosc is None
        and dzialka.ogrodzenie is None
        and dzialka.uzbrojenie is None
        and dzialka.drzewa is None
        and dzialka.rodzaj_gleby is None
    )


# określenie danych ogrodzenia z parametryzacją
@pytest.mark.parametrize("rodzaj, przewidywanie", [("zwykły", 12600), ("drogi", 21000)])
# test kosztu ogrodzenia
def test_dzialka_koszt_ogrodzenia(dzialka, rodzaj, przewidywanie):
    assert dzialka.koszt_ogrodzenia(rodzaj) == przewidywanie


# określenie danych działki z parametryzacją
@pytest.mark.parametrize(
    "szerokosc, dlugosc, ogrodzenie, uzbrojenie, drzewa, rodzaj_gleby, standard_plotu, ilosc_drzew, przewidywanie",
    [
        (30, 40, False, False, True, "glina", "zwykły", 5, 28400),
        (20, 30, True, True, False, "ziemia", "drogi", 0, 0),
    ],
)
# test kosztu przygotowania pod budowę
def test_dzialka_koszt_przygotowania_pod_budowe(
    szerokosc,
    dlugosc,
    ogrodzenie,
    uzbrojenie,
    drzewa,
    rodzaj_gleby,
    standard_plotu,
    ilosc_drzew,
    przewidywanie,
):
    dzialka = Dzialka(szerokosc, dlugosc, ogrodzenie, uzbrojenie, drzewa, rodzaj_gleby)
    assert (
        dzialka.koszt_przygotowania_pod_budowe(standard_plotu, ilosc_drzew)
        == przewidywanie
    )


class TestStanDomu:
    def test_dom_stan_poczatkowy(self):
        dom = Dom(10, 8, 2, 5, 6, True, False, True, "standardowy")
        assert dom.state == "Dane podane"

    def test_dom_stan_reset(self):
        dom = Dom(10, 8, 2, 5, 6, True, False, True, "standardowy")
        dom.reset()
        assert dom.state == "Brak danych"


class TestStanDzialki:
    def test_dzialka_stan_poczatkowy(self):
        dzialka = Dzialka(20, 30, True, False, True, "ziemia")
        assert dzialka.state == "Dane podane"

    def test_dzialka_stan_reset(self):
        dzialka = Dzialka(20, 30, True, False, True, "ziemia")
        dzialka.reset()
        assert dzialka.state == "Brak danych"
