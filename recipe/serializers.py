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

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5. ")
        return value


