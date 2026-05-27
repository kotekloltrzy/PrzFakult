# Program do szacowania kosztu budowy domu
Napisany w Pythonie program który szacuje koszty budowy domu i związanych z tym dodatkowych kosztów budowlanych

# Opis działania programu
Po uruchomieniu, użytkownikowi wyświetla się menu główne z którego poziomu można wykonać następujące akcje:
 1. Podaj dane domu
 2. Podaj dane działki
 3. Pokaż koszty
 4. Przewidywany czas wykonania
 5. Zresetuj dane domu
 6. Zresetuj dane działki
 0. Wyjśćie

Użytkownik wybiera którą opcję chce wybrać poprzez podanie adekwatnej do akcji liczby

### Dane jakie przyjmuje dom:
 - długość
 - szerokość
 - liczba pięter 
 - liczba pokoi
 - ilość okien
 - rodzaj
 - garaż
 - piwnica
 - poddasze
 - rodzaj

### Dane jakie przyjmuje działka:
 - długość
 - szerokość
 - ogrodzenie
 - uzbrojenie
 - drzewa
 - rodzaj gleby

 Żeby użytkownik mógł zobaczyć koszt lub czas budowy musi najpierw podać dane domu oraz działki

 # Struktura projektu

```
.
└── Fakultet/
    ├── src/
    │   ├── dzialania.py
    │   ├── klasy.py
    │   └── menu.py
    ├── tests/
    │   ├── test_dzialania.py
    │   ├── test_klasy.py
    │   └── test_menu.py
    ├── main.py
    ├── requirements.txt
    └── README.md
```

# Uruchamianie testów

Uruchom wszystkie test za pomocą:
```
pytest
```

Test dla konkretnego pliku np.:
```
pytest tests/test_klasy.py
```

# Sprawdzanie jakości kodu

### Używanie Pylint:
```
pylint src/ tests/ main.py
```

### Używanie Flake8:
```
flake8 src/ tests/ main.py
```

Oba testery są skonfigurowane w ```setup.cfg```
