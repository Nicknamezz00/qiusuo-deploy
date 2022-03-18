from django.urls import path, include

from rest_framework import routers

from subjects import views

subject_api_router = routers.DefaultRouter()

subject_api_router.register('subjects', views.SubjectViewSet,
                            basename='subjects')

urlpatterns = [
    path('', include((subject_api_router.urls, 'subjects'),
                     namespace='subjects')),

]
