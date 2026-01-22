## ORM Relationships

This app demonstrates Django ORM relationships:

- Author → Book (ForeignKey)
- Library → Book (ManyToMany)
- Library → Librarian (OneToOne)

### Sample Queries:

1. Get all books by an author:
```python
books_by_author("Author Name")
books_in_library("Library Name")
librarian_for_library("Library Name")
