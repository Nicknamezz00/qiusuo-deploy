from django.urls import path, include
from rest_framework import routers

from favorite.views import favorite_api

favorite_api_router = routers.DefaultRouter()

favorite_api_router.register('favorites',
                             favorite_api.UserFavoriteFolderViewSet,
                             basename='userFavorite')

urlpatterns = [
    path('', include((favorite_api_router.urls, 'favorite'), namespace='favorites'))
]
