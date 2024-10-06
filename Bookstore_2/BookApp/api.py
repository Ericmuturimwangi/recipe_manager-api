from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel


@api_view(["GET"])
def BookListApi(request):
    # fetch data from db
    books = BookModel.objects.all()
    # convert to json because of the api
    books = [
        {
            "name": book.name,
            "author": book.author,
        }
        for book in books
    ]

    return Response(books)


# POST request
@api_view(["POST"])
def BookCreateApi(request):
    # get data and post data in the db
    data = request.data

    name = data["name"]
    author = data["author"]

    BookModel(name=name, author=author).save()

    return Response({"message": "Book Created"})
