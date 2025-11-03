from library import Book, Library  # Importujemy klasy logiki domenowej

def print_menu():
    """Wyświetla główne menu programu."""
    # Proste menu tekstowe z dostępnymi akcjami
    print("\n--- System Zarządzania Biblioteką ---")
    print("1. Dodaj nową książkę")             
    print("2. Wypożycz książkę")                
    print("3. Zwróć książkę")                   
    print("4. Wyświetl listę wszystkich książek") 
    print("5. Zakończ")
    print("---------------------------------")

def main():
    """Główna funkcja programu, obsługująca pętlę i interfejs."""
    # Tworzymy bibliotekę i dodajemy kilka początkowych książek
    my_library = Library()

    my_library.add_book(Book("Władca Pierścieni", "J.R.R. Tolkien", 1954))
    my_library.add_book(Book("Hobbit", "J.R.R. Tolkien", 1937))
    my_library.add_book(Book("Diuna", "Frank Herbert", 1965))

    # Główna pętla wprowadzania poleceń użytkownika
    while True:
        print_menu()
        choice = input("Wybierz opcję (1-5): ")

        if choice == '1':  # Dodanie nowej książki
            title = input("Podaj tytuł: ")
            author = input("Podaj autora: ")
            try:
                year = int(input("Podaj rok wydania: "))
                new_book = Book(title, author, year)
                my_library.add_book(new_book)
            except ValueError:
                print("\nBłąd: Rok musi być liczbą. Spróbuj ponownie.")
        
        elif choice == '2':  # Wypożyczenie książki
            my_library.list_books() 
            title = input("\nPodaj tytuł książki do wypożyczenia: ")
            my_library.borrow_book(title)

        elif choice == '3':  # Zwrot książki
            title = input("Podaj tytuł książki do zwrotu: ")
            my_library.return_book(title)

        elif choice == '4':  # Wyświetlenie listy książek
            my_library.list_books()

        elif choice == '5':  # Wyjście
            print("Do widzenia!")
            break
        
        else:
            print("\nNieprawidłowa opcja. Wybierz numer od 1 do 5.")

if __name__ == "__main__":
    main()