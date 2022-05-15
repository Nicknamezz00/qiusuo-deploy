from django.urls import path, include
from rest_framework import routers

from scratch.views import ScratchViewSet

scratch_api_router = routers.DefaultRouter()

scratch_api_router.register(r'scratch', ScratchViewSet, basename='scratch')

urlpatterns = [
    path('', include((scratch_api_router.urls, 'scratch'), namespace='scratch')),
]
