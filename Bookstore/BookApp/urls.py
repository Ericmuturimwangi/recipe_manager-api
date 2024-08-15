from django.urls import path
from .api import BookListApi, BookCreateAPi

urlpatterns = [
    path("list", BookListApi),
    path("create", BookCreateAPi),
]
