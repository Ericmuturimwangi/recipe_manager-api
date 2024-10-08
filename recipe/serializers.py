from .models import Recipe, FavoriteRecipe,Review
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class FavoriteRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model= FavoriteRecipe
        fields = ['user', 'recipe', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'recipe', 'rating', 'comment', 'created_at']


