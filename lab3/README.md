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

## Hosting na PythonAnywhere

Instrukcja wdrożenia aplikacji jako prostego serwisu WWW:

1. Zaloguj się na PythonAnywhere i otwórz konsolę Bash.
2. Sklonuj repozytorium:
   - `git clone https://github.com/resccrew/MikitaPravoraulab3.git`
3. Przejdź do folderu projektu i (opcjonalnie) utwórz wirtualne środowisko:
   - `cd MikitaPravoraulab3/lab3`
   - `python3 -m venv .venv && source .venv/bin/activate`
4. Zainstaluj zależności:
   - `pip install -r requirements.txt`
5. W panelu „Web” utwórz nową aplikację Flask (Python 3.x).
6. W pliku WSGI ustaw aplikację na:
   ```python
   import sys
   path = '/home/<twoja_nazwa_użytkownika>/MikitaPravoraulab3/lab3'
   if path not in sys.path:
       sys.path.append(path)

   from app import app as application
   ```
7. Ustaw „Source code” na folder `MikitaPravoraulab3/lab3`.
8. Zrestartuj aplikację w panelu Web — po chwili strona powinna działać.

Uwaga: Stan biblioteki jest w pamięci procesu (demo). Do trwałości danych potrzebna baza (np. SQLite).