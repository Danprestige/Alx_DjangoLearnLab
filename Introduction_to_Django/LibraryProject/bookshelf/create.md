# Create Operation

```python
from bookshelf.models import Book

# Create a Book instance
book1 = Book(title="1984", author="George Orwell", publication_year=1949)
book1.save()  # Output: None (book successfully created)
