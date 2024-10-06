from django.db import models
from rest_framework import filters
from dajngo.filters.rest_framework import DjangoFilterBackend


class Recipe(models.Model):
    title =  models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
