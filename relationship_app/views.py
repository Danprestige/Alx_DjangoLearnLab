# relationship_app/views.py
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library

# ----------------------------
# Function-based view: list all books
# ----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# ----------------------------
# Class-based view: show library details + books
# ----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# ----------------------------
# Registration view
# ----------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in automatically after registration
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# ----------------------------
# Login view
# ----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("list_books")
        else:
            return render(request, "relationship_app/login.html", {"form": {}, "error": "Invalid credentials"})
    return render(request, "relationship_app/login.html", {"form": {}})

# ----------------------------
# Logout view
# ----------------------------
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
