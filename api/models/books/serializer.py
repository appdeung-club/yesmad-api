from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.books import Book


class BookSerializer(DocumentSerializer):
    class Meta:
        model = Book
        fields = Book.fields