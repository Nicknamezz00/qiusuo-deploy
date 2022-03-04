from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, JSONWebTokenAPIView

from operations.views.user_operations.register import RegisterViewSet, SendSmsVerifyCodeViewSet

operations_api_router = routers.DefaultRouter()

operations_api_router.register('register', RegisterViewSet,
                               basename='register')
operations_api_router.register('verify-code', SendSmsVerifyCodeViewSet,
                               basename="verify-code")
urlpatterns = [
    path('', include((operations_api_router.urls, 'operations'), namespace='operations')),
    path('login/', obtain_jwt_token, name='login'),
]
