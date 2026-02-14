from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm


def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get("q")
        if query:
            books = Book.objects.filter(title__icontains=query)

    return render(request, "bookshelf/book_list.html", {
        "form": form,
        "books": books
    })

"""
This view uses Django ORM filtering to prevent SQL injection.
User input is validated using Django Forms.
"""
