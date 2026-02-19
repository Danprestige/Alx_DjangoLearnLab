from django.shortcuts import render
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def search_books(request):
    query = request.GET.get('q')

    if query:
        # SAFE: Django ORM automatically parameterizes queries
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'bookshelf/book_list.html', {'books': books})
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

def book_list(request):
    # Use the ORM's .all() or .filter() to safely fetch data
    books = Book.objects.all() 
    return render(request, 'bookshelf/book_list.html', {'books': books})

def search_books(request):
    # SECURE: Use Django ORM's filter which parameterizes input
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})