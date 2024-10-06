from django.shortcuts import render
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filter.OrderingFilter)
    filterset_fields = ['ingredients', 'category']
    search_fields = ['title']
    ordering_fields = ['created_at', 'updated_at']



