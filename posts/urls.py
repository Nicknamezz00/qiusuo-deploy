from django.urls import path, include
from rest_framework import routers

from posts.views import post_api

post_api_router = routers.DefaultRouter()

post_api_router.register(r'posts', post_api.PostViewSet, basename='posts')

urlpatterns = [
    path('', include((post_api_router.urls, 'posts'), namespace='posts')),
]