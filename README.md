## ORM Relationships - relationship_app

This app demonstrates Django ORM relationships:

- Author → Book (ForeignKey)
- Library → Book (ManyToMany)
- Library → Librarian (OneToOne)

### Sample Queries:

1. Get all books by an author:
```python
from relationship_app.query_samples import books_by_author
books_by_author("Author Name")
