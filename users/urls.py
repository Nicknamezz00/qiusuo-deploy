from django.urls import path, include
from rest_framework import routers

from users.views import user_api

user_api_router = routers.DefaultRouter()

user_api_router.register('users', user_api.UserInfoViewSet, basename='users')
user_api_router.register('titles', user_api.UserTitleViewSet, basename='titles')

urlpatterns = [
    path('', include((user_api_router.urls, 'users'), namespace='users'))
]
