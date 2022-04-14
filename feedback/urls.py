from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import feedback_api

feedback_api_router = DefaultRouter()

feedback_api_router.register('feedback', feedback_api.FeedbackViewSet, basename='feedback')

feedback_api_router.register('feedback_reply', feedback_api.FeedbackReplyViewSet, basename='feedback_reply')

urlpatterns = [
    path('', include(feedback_api_router.urls)),
]