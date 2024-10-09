from django.shortcuts import render
from .models import Recipe, FavoriteRecipe, Review
from .serializers import RecipeSerializer, FavoriteRecipeSerializer, ReviewSerializer
from rest_framework import viewsets, status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrOwner
from rest_framework.response import Response
from rest_framework.decorators import action
from .hybrid_recommendations import hybrid_recommendations
from rest_framework.views import APIView
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['ingredients', 'category']
    search_fields = ['title']
    ordering_fields = ['created_at', 'updated_at']
    permission_classes= [IsAuthenticated, IsAdminOrOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) #check whether the user is the owner of the recipe

    def destroy(self, request, *args, **kwargs):
        # only admins and owners can delete the recipes
        recipe = self.get_object()
        if request.user != recipe.owner and not request.user.groups.filter(name='Admin').exists():
            return Response({'error':'You do not have the permission to del this recipe'}, status=403)
        
        return super().destroy(request, *args, **kwargs)
    
    def schedule(self, request, *args, **kwargs):
        recipe= self.get_object()
        if request.user != recipe.owner and not request.user.groups.filter(name='Admin').exists():
            return Response({'error':'You do not have the ability to schedule a recipe'}, status=status.HTTP_403_FORBIDDEN)
        
        recipe.is_scheduled = True
        recipe.save()

        return Response({'message': 'Recipe scheduled successfully'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def get_recommendations(self, request):
     
        recommended_recipes = []
        return Response(recommended_recipes)
    


class FavoriteRecipeViewSet(viewsets.ModelViewSet):
    queryset=FavoriteRecipe.objects.all()
    serializer_class = FavoriteRecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        recipe_pk=self.kwargs['recipe_pk']
        return Review.objects.filter(recipe_id=recipe_pk)
    

class RecipeRecommendationView(APIView):
       
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recommendations = hybrid_recommendations(request.user)
        # Serialize the recommended recipes
        serializer = RecipeSerializer(recommendations, many=True)  # Assuming you have a RecipeSerializer
        return Response(serializer.data, status=200)
    





