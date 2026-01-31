from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField(null=True, blank=True)
    libraries = models.ManyToManyField('Library', related_name='books')  # string reference

    def __str__(self):
        return self.title
