from django.shortcuts import render
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['ingredients', 'category']
    search_fields = ['title']
    ordering_fields = ['created_at', 'updated_at']
    permission_classess= [IsAuthenticated]



