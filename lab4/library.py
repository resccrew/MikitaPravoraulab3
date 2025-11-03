

class Book:
    """
    Reprezentuje pojedynczą książkę w bibliotece.
    Zgodnie ze schematem[cite: 42, 64].
    """
    def __init__(self, title, author, year):
        # Pola książki: tytuł, autor, rok i status dostępności
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def __str__(self):
        """Zwraca czytelną reprezentację obiektu książki."""
        status = "Dostępna" if self.is_available else "Wypożyczona"
        return f'"{self.title}", {self.author} ({self.year}) - Stan: {status}'

    def borrow_book(self):
        """Oznacza książkę jako wypożyczoną, jeśli jest dostępna."""
        if self.is_available:
            self.is_available = False
            return f"Książka '{self.title}' została pomyślnie wypożyczona."
        else:
            return f"Książka '{self.title}' jest już wypożyczona."

    def return_book(self):
        """Oznacza książkę jako zwróconą (dostępną)."""
        if not self.is_available:
            self.is_available = True
            return f"Książka '{self.title}' została zwrócona."
        else:
            return f"Książka '{self.title}' była już dostępna w bibliotece."


class Library:
    """
    Reprezentuje bibliotekę, która zarządza zbiorem obiektów Book.
    Zgodnie ze schematem[cite: 49].
    """
    def __init__(self):
        # Prosta lista — magazyn wszystkich książek
        self.books = []

    def add_book(self, book):
        """Dodaje nową książkę (obiekt Book) do biblioteki."""
        self.books.append(book)
        print(f"\nDodano książkę: {book.title}")

    def list_books(self):
        """Wyświetla listę wszystkich książek w bibliotece[cite: 28]."""
        if not self.books:
            print("\nBiblioteka jest pusta.")
            return

        print("\n--- Lista książek w bibliotece ---")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("---------------------------------")

    def find_book(self, title):
        """Pomocnicza metoda do wyszukiwania książki po tytule."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        """Wypożycza książkę o podanym tytule."""
        book = self.find_book(title)
        if book:
            print(book.borrow_book())
        else:
            print(f"\nNie znaleziono książki o tytule '{title}'.")

    def return_book(self, title):
        """Zwraca książkę o podanym tytule."""
        book = self.find_book(title)
        if book:
            print(book.return_book())
        else:
            print(f"\nNie znaleziono książki o tytule '{title}'.")