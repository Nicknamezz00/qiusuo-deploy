from informations import views
from rest_framework import routers
from django.urls import path, include

informations_router = routers.DefaultRouter()

informations_router.register('schools', views.SchoolViewSet,
                             basename='schools')

urlpatterns = [
    path('', include((informations_router.urls,
                      'informations'),
                     namespace='informations'))]
