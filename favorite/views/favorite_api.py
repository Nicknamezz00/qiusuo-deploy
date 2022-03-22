from rest_framework.viewsets import ModelViewSet

from favorite.models import UserFavorite, UserFavoriteFolder
from favorite.serializers import UserFavoriteSerializer, UserFavoriteFoldSerializer


class UserFavoriteFolderViewSet(ModelViewSet):

    queryset = UserFavoriteFolder.objects.all()
    serializer_class = UserFavoriteFoldSerializer
