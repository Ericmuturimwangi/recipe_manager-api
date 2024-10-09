from django.db import models
from .models import Recipe

def content_based_reccomendations(favorite_recipes_ids):
    favorite_recipes = Recipe.objects.filter(id__in=favorite_recipes_ids)
    favorite_categories = favorite_recipes.values_list('category', flat=True)


    recommended_recipes = Recipe.objects.filter(
        models.Q(category__in=favorite_categories)
    ).exclude(id__in=favorite_recipes_ids).distinct()

    return recommended_recipes