import datetime

from mongoengine import Document, DateTimeField, StringField, DateField, EmailField, ListField, ReferenceField, URLField

from api.utils.fields import PasswordField


class User(Document):
    fields = ['userId', 'password', 'name', 'email', 'friends_ids', 'imageUrl']
    meta = {'collection': 'users'}

    createdTime = DateTimeField(default=datetime.datetime.now())
    updatedTime = DateTimeField(default=datetime.datetime.now())
    userId = StringField(min_length=4, max_length=16)
    password = PasswordField(algorithm=PasswordField.ALGORITHM_SHA256)
    birthday = DateField()
    name = StringField(max_length=32)
    email = EmailField(max_length=64, unique=True)
    friends_ids = ListField(ReferenceField('self'))
    imageUrl = URLField()
