<<<<<<< HEAD
from .models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  # ✅ ALX expects objects.filter
    except Author.DoesNotExist:
        return []

# 2️⃣ List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3️⃣ Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)  # ✅ ALX expects this format
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

=======
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
>>>>>>> 41a6af3 (ALX Django Models Task)
