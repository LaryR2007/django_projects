from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('books:book-detail', args=[str(self.id)])


# Create your models here.
