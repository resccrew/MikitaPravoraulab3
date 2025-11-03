# Lab3 — Biblioteka (Python)

Prosty projekt konsolowy do zarządzania biblioteką: dodawanie książek, wypożyczanie i zwroty.

## Struktura projektu

- `library.py` — logika modelu domenowego (klasy `Book` i `Library`).
- `main.py` — punkt wejścia, interfejs konsolowy.
- `tests/` — testy jednostkowe dla `library.py`.
- `requirements.txt` — zależności projektu (obecnie brak).
- `.gitignore` — standardowe wykluczenia dla projektu w Pythonie.

## Uruchomienie

1. Upewnij się, że masz zainstalowanego Pythona `3.10+` (u Ciebie: `3.13.2`).
2. (Opcjonalnie) utwórz wirtualne środowisko:
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `python -m venv .venv; .venv\\Scripts\\Activate.ps1`
3. Zainstaluj zależności (jeśli się pojawią): `pip install -r requirements.txt`
4. Uruchom program: `python3 main.py`

## Testy

Uruchomienie testów jednostkowych:

```bash
python3 -m unittest -q
```

## Uwagi

- Projekt nie wymaga zewnętrznych bibliotek; cały kod korzysta ze standardowej biblioteki Pythona.
- W razie potrzeby można spakietować projekt i dodać `pyproject.toml`/`setup.cfg`.