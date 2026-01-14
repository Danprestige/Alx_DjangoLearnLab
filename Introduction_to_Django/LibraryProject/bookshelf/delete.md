
---

# **4️⃣ delete.md**

```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book
book1 = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book1.delete()

# Verify deletion
Book.objects.all()
# Output: (1, {'bookshelf.Book': 1})
#         <QuerySet []>
