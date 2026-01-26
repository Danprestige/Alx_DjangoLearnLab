from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

<<<<<<< HEAD
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
=======

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
>>>>>>> 41a6af3 (ALX Django Models Task)

    def __str__(self):
        return self.title

<<<<<<< HEAD
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
=======

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
>>>>>>> 41a6af3 (ALX Django Models Task)

    def __str__(self):
        return self.name

<<<<<<< HEAD
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
=======

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
>>>>>>> 41a6af3 (ALX Django Models Task)

    def __str__(self):
        return self.name
