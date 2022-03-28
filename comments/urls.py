from django.urls import include, path
from rest_framework.routers import DefaultRouter

from comments.views import comment_api

comment_api_router = DefaultRouter()

comment_api_router.register('comments', comment_api.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(comment_api_router.urls)),
]