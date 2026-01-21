from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Author, Book

class AuthorListView(ListView):
    model = Author
    template_name = "relationship_app/author_list.html"
    context_object_name = "authors"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "relationship_app/author_detail.html"
    context_object_name = "author"

class BookListView(ListView):
    model = Book
    template_name = "relationship_app/book_list.html"
    context_object_name = "books"

