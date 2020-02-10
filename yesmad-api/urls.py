from django.conf.urls import include, url
from rest_framework import routers

from api.models.books.view import BookViewSet
from api.models.users.view import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'books', BookViewSet, base_name='books')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
