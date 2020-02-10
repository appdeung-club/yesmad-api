from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models.users import User


class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = User.fields

