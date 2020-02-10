from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from api.models.users import User
from api.models.users.serializer import UserSerializer


class UserViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()
