from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import time

class Extra_user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    document_type = models.CharField(max_length=50)
    document_number = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=10)
    def __str__(self):
        return self.user.username

class Language(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Country (models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Editor(models.Model):
  name = models.CharField(max_length=50)
  country  = models.ForeignKey(Country, on_delete=models.CASCADE)
  def __str__(self):
      return self.name

class Genre (models.Model):
  type =  models.CharField(max_length=50)
  def __str__(self):
      return self.type

class Author(models.Model):
    first_name =  models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    death_date = models.DateField()
    note = models.TextField()
    sex = models.TextChoices('Uomo', 'Donna')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.last_name + " " + self.first_name

class Sezione(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=14 )
    book_name = models.CharField(max_length=200)
    book_plot = models.TextField()
    book_pages_number = models.IntegerField()
    book_release_date = models.DateField(null=True, blank=True)
    book_image = models.ImageField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, null=True)
    author = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    sezione = models.ForeignKey(Sezione, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.book_name

class Volume(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateField(null=True, blank=True)
    dismission_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.book.book_name

class Loan(models.Model):
  return_date = models.DateTimeField(blank=True, null=True)
  borrow_date = models.DateTimeField(default=datetime.now())
  user  = models.ForeignKey(User, on_delete=models.CASCADE)
  volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
  prolungato = models.BooleanField(default=False)
