from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
book

# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

