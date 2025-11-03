# System zarządzania biblioteką (lab3)

Prosty projekt konsolowy do zarządzania książkami w bibliotece: dodawanie, wypożyczanie i zwroty.

## Struktura projektu

- `library.py` — logika modelu domenowego (klasy `Book` i `Library`).
- `main.py` — punkt wejścia, interfejs konsolowy.
- `tests/` — testy jednostkowe dla `library.py`.
- `requirements.txt` — zależności projektu (obecnie nie są wymagane).
- `.gitignore` — standardowe wykluczenia dla projektu Python.

## Uruchomienie

1. Upewnij się, że masz zainstalowany Python 3.10+.
2. (Opcjonalnie) utwórz wirtualne środowisko:
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `python -m venv .venv; .venv\\Scripts\\Activate.ps1`
3. Zainstaluj zależności (jeśli się pojawią): `pip install -r requirements.txt`
4. Uruchom program: `python3 main.py`

## Testy

Aby uruchomić testy jednostkowe:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -q
```

## Uwagi

- Projekt nie wymaga zewnętrznych bibliotek; cały kod korzysta ze standardowej biblioteki Pythona.
- W razie potrzeby można przygotować pakiet i dodać `pyproject.toml`/`setup.cfg`.