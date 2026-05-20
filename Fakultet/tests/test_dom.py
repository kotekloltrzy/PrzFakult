import pytest
from src.dom import Dom, Poddasze, Garaz, Piwnica


# określenie danych domu
@pytest.fixture
def dom():
    return Dom(9.5, 7.5, 2, 10, True, True, True, "standardowy")


# test resetowania danych domu
def test_reset(dom):
    dom.reset()
    assert (dom.szerokosc is None and dom.dlugosc is None and dom.liczba_pieter is None and dom.ilosc_okien is None and
            dom.garaz is None and dom.piwnica is None and dom.poddasze is None and dom.rodzaj is None)


# określenie danych poddasza z parametryzacją
@pytest.mark.parametrize(
    "rodzaj, przewidywane",
    [
        ("mieszkalne", 106875),
        ("magazynowe", 26718.75)
    ]
)
# test kosztu poddasza
def test_poddasze_koszt(dom, rodzaj, przewidywane):
    poddasze = Poddasze(rodzaj, dom)
    assert poddasze.koszt() == przewidywane


# określenie danych piwnicy z parametryzacją
@pytest.mark.parametrize(
    "rodzaj, przewidywane",
    [
        ("użytkowa", 199500),
        ("magazynowa", 142500)
    ]
)
# test kosztu piwnicy
def test_piwnica_koszt(dom, rodzaj, przewidywane):
    piwnica = Piwnica(rodzaj, dom)
    assert piwnica.koszt() == przewidywane


# określenie danych garażu z parametryzacją
@pytest.mark.parametrize(
    "rodzaj, ilosc_aut, przewidywane",
    [
        ("wolnostojący", "2", 340000),
        ("dobudowany", "1", 180000)
    ]
)
# test kosztu garażu
def test_garaz_koszt(rodzaj, ilosc_aut, przewidywane):
    garaz = Garaz(rodzaj, ilosc_aut)
    assert garaz.koszt() == przewidywane
