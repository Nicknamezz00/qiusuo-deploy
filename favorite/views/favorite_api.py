from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from favorite.models import UserFavorite, UserFavoriteFolder
from favorite.serializers import UserFavoriteSerializer, UserFavoriteFoldSerializer


class UserFavoriteFolderViewSet(ModelViewSet):

    def list(self, request, *args, **kwargs):
        """
        此接口仅能获取关于自己的信息
        """
        queryset = self.filter_queryset(self.get_queryset())
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    queryset = UserFavoriteFolder.objects.all().order_by('create_at')
    serializer_class = UserFavoriteFoldSerializer
    permission_classes = [IsAuthenticated]


class UserFavoriteViewSet(ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer
    permission_classes = [IsAuthenticated]
