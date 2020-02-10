from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from api.models.books import Book
from api.models.books.serializer import BookSerializer


class BookViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
