from django.db import models

# Create your models here.


class BookModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
