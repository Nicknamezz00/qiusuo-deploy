from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from favorite.models import UserFavorite, UserFavoriteFolder
from favorite.serializers import UserFavoriteSerializer, UserFavoriteFoldSerializer


class UserFavoriteFolderViewSet(ModelViewSet):
    queryset = UserFavoriteFolder.objects.all().order_by('create_at')
    serializer_class = UserFavoriteFoldSerializer


class UserFavoriteViewSet(ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer