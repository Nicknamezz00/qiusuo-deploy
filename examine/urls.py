from django.urls import path, include
from rest_framework import routers

from examine.views import title_examine_api

examine_title_api_router = routers.DefaultRouter()

examine_title_api_router.register(
    r'title-examine',
    title_examine_api.TitleExamineViewSet,
    basename='title-examine')

urlpatterns = [
    path('', include(examine_title_api_router.urls)),
]
