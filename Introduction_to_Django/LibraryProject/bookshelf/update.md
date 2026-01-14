
---

# **3️⃣ update.md**

```markdown
# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book (if not already in variable)
book1 = Book.objects.get(title="1984")

# Update the title
book1.title = "Nineteen Eighty-Four"
book1.save()

# Verify update
Book.objects.all()
# Output: <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
