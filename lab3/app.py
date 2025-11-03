from flask import Flask, render_template, request, redirect, url_for, flash
from library import Library, Book

app = Flask(__name__)
app.secret_key = "dev-secret"

# Inicjalna biblioteka z kilkoma książkami
library = Library()
library.add_book(Book("Pan Tadeusz", "Adam Mickiewicz", 1834))
library.add_book(Book("Lalka", "Bolesław Prus", 1890))
library.add_book(Book("Quo Vadis", "Henryk Sienkiewicz", 1896))


@app.route("/")
def index():
    return render_template("index.html", books=library.list_books())


@app.route("/add", methods=["POST"])
def add_book():
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    year = request.form.get("year", "").strip()

    if not title or not author or not year.isdigit():
        flash("Podaj poprawny tytuł, autora i rok.")
        return redirect(url_for("index"))

    library.add_book(Book(title, author, int(year)))
    flash("Książka dodana.")
    return redirect(url_for("index"))


@app.route("/borrow", methods=["POST"])
def borrow_book():
    title = request.form.get("title", "").strip()
    try:
        library.borrow_book(title)
        flash("Wypożyczono książkę.")
    except ValueError as e:
        flash(str(e))
    return redirect(url_for("index"))


@app.route("/return", methods=["POST"])
def return_book():
    title = request.form.get("title", "").strip()
    try:
        library.return_book(title)
        flash("Zwrócono książkę.")
    except ValueError as e:
        flash(str(e))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)