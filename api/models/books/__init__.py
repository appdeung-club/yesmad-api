import datetime

from mongoengine import Document, DateTimeField, StringField, URLField


class Book(Document):
    fields = ['title', 'author', 'publisher', 'isbn', 'image']
    meta = {'collection': 'books'}

    createdTime = DateTimeField(default=datetime.datetime.now())
    updatedTime = DateTimeField(default=datetime.datetime.now())
    title = StringField(max_length=64)
    author = StringField(max_length=32)
    publisher = StringField(max_length=32)
    isbn = StringField(max_length=32)
    image = URLField()
