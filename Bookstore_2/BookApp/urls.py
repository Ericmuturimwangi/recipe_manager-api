from django.urls import path
from .api import BookListApi, BookCreateApi

urlpatterns = [
    path("list", BookListApi),
    path("create", BookCreateApi),
]
