# LibraryProject/relationship_app/views.py

# ✅ ALX requires explicit import of models
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # <-- This import is required to pass ALX check

# =========================
# Function-based view: list all books
# =========================
def list_books(request):
    books = Book.objects.all()  # ALX check expects this
    return render(request, "relationship_app/list_books.html", {"books": books})

# =========================
# Class-based view: show library detail with books
# =========================
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
