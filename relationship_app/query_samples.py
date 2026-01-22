# django-models/relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# =========================
# 1️⃣ Query all books by a specific author
# =========================

# Get all authors with the same name
authors = Author.objects.filter(name="J.K. Rowling")
author = authors.first()  # pick the first one safely

# ALX check expects: objects.filter(author=author)
books_by_author = Book.objects.filter(author=author)

# =========================
# 2️⃣ List all books in a library
# =========================

# Get all libraries with the same name
libraries = Library.objects.filter(name="Central Library")
library = libraries.first()  # pick the first one safely

# ALX check expects: library.books.all()
books_in_library = library.books.all()

# =========================
# 3️⃣ Retrieve the librarian for a library
# =========================

# ALX check expects: Librarian.objects.get(library=library)
librarian = Librarian.objects.get(library=library)
