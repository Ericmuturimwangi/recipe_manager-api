from django.db import models
from .models import FavoriteRecipe,Recipe

def collaborative_reccomendations(user):
    user_favorites = FavoriteRecipe.objects.filter(user=user).values_list('recipe_id', flat=True)

    similar_users = FavoriteRecipe.objects.filter(recipe_id__in=user_favorites).exclude(user=user)
    similar_users_ids = similar_users.values_list('user_id', flat=True)

    recommended_recipes = FavoriteRecipe.objects.filter(
        user_id__in=similar_users_ids
    ).exclude(recipe_id__in=user_favorites).values_list('recipe_id', flat=True)

    return Recipe.objects.filter(id__in=recommended_recipes)
