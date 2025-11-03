import unittest

from library import Book, Library


class TestBook(unittest.TestCase):
    def test_initial_state(self):
        b = Book("Test", "Author", 2024)
        self.assertTrue(b.is_available)

    def test_borrow_then_return(self):
        b = Book("Test", "Author", 2024)
        msg_borrow = b.borrow_book()
        self.assertFalse(b.is_available)
        self.assertIn("wypożyczona", msg_borrow.lower())

        msg_return = b.return_book()
        self.assertTrue(b.is_available)
        self.assertIn("zwrócona", msg_return.lower())


class TestLibrary(unittest.TestCase):
    def test_add_and_find_book(self):
        lib = Library()
        b = Book("Diuna", "Frank Herbert", 1965)
        lib.add_book(b)
        found = lib.find_book("Diuna")
        self.assertIs(found, b)

    def test_borrow_and_return_flow(self):
        lib = Library()
        b = Book("Hobbit", "J.R.R. Tolkien", 1937)
        lib.add_book(b)
        lib.borrow_book("Hobbit")
        self.assertFalse(b.is_available)
        lib.return_book("Hobbit")
        self.assertTrue(b.is_available)


if __name__ == "__main__":
    unittest.main()