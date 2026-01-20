from relationship_app.models import Author, Book, Library, Librarian

# ✅ 1. Query all books by a specific author
authors = Author.objects.filter(name="J.K. Rowling")
author = authors.first()  # pick the first if there are duplicates
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# ✅ 2. List all books in a library
libraries = Library.objects.filter(name="Central Library")
library = libraries.first()
books_in_library = library.books.all()
print(books_in_library)

# ✅ 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(librarian)
