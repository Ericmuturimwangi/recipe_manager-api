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
    # is_scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    
class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user', 'recipe') #preventing the duplication of favorites.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range (1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    schedule_for=models.DateField()
    time = models.TimeField()
    difficulty = models.CharField(max_length=255, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    prep_time = models.IntegerField(help_text="Preparation Time in minutes")


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe') #prevents duplicate reviews

class UserActivity(models.Model):
    ACTION_CHOICES=[
        ('view', 'Viewed Recipe'),
        ('favorite', 'Favorited Recipe'),
        ('review', 'submitted Review'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=25, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.user.username} {self.action} {self.recipe.title if self.recipe else''} at {self.timestamp}")