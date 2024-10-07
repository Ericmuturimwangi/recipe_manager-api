from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title =  models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length = 255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.title
    
    
