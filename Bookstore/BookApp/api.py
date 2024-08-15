from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel


# used decorator and mention the request to pass
@api_view(["GET"])
def BookListApi(request):
    # fetch this from the db and send response
    # books = [
    #     {
    #         "name": "theDifference",
    #         "author": "Eric Muturi",
    #     },
    #     {
    #         "name": "From Trenches to Console",
    #         "author": "Eric Muturi",
    #     },
    #     {
    #         "name": "God of the Mountains",
    #         "author": "Eric Muturi",
    #     },
    # ]

    books = BookModel.objects.all()

    books = [
        {
            "name": book.name,
            "author": book.author,
        }
        for book in books
    ]

    return Response(books)

    # Post request fetch data from the bodya nd add it to the db


@api_view(["POST"])
def BookCreateAPi(request):
    data = request.data

    name = data["name"]
    author = data["author"]

    BookModel(name=name, author=author).save()

    return Response({"message": "Book Created"})
