from django.contrib import admin
from .models import Book  # import the Book model from models.py

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns in admin
    list_filter = ('publication_year',)                      # ✅ ALX check
    search_fields = ('title', 'author')                      # searchable fields

admin.site.register(Book, BookAdmin)
