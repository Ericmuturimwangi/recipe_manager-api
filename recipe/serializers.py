from .models import Recipe, FavoriteRecipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class FavoriteRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model= FavoriteRecipe
        fields = ['user', 'recipe', 'created_at']
        

