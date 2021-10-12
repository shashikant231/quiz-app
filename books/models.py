from django.db import models

# Create your models here.
class BookList(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.book_name

