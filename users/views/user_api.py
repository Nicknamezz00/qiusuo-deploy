from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.models import UserInfo
from users.serializers import UserProfileSerializer


class UserInfoViewSet(ModelViewSet):
    """
    Only superuser are allowed the following methods.
        GET   /api/users/           Return all users.
        GET   /api/users/<pk>/      Return a user with pk=<pk>.
        POST  /api/users/           Create a new user.
        PUT   /api/users/<pk>/      Update a user.
        PATCH /api/users/<pk>/      Update a user.
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['id', 'username', 'qq', 'email', 'phone']
    ordering_fields = ['id', 'username', 'created_at']
