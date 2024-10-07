from django.shortcuts import render
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrOwner
from rest_framework.response import Response
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






