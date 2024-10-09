from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from recipe.models import Recipe, FavoriteRecipe,UserActivity
from recipe.serializers import RecipeSerializer, ReviewSerializer
from rest_framework import status
class RecipeDetailView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        # Log the activity
        UserActivity.objects.create(user=request.user, recipe=recipe, action='view')

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    
class FavoriteRecipeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)

        # Log the activity
        UserActivity.objects.create(user=request.user, recipe=recipe, action='favorite')
        return Response({'message': 'Recipe favorited'}, status=201)
    
class ReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        
        if recipe.reviews.filter(user=request.user).exists():
            return Response({'error': 'You have already reviewed this recipe.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, recipe=recipe)

            # Log the activity
            UserActivity.objects.create(user=request.user, recipe=recipe, action='review')

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')

        activity_data = []
        for activity in activities:
            activity_data.append({
                'action': activity.action,
                'recipe': activity.recipe.title if activity.recipe else None,
                'timestamp': activity.timestamp,
            })

        return Response(activity_data, status=200)