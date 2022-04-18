from django.urls import path, include
from rest_framework import routers

from operations.views.user_operations.login import LoginViewSet
from operations.views.user_operations.register import RegisterViewSet
from operations.views.user_operations.send_code import SendSmsVerifyCodeViewSet

operations_api_router = routers.DefaultRouter()

operations_api_router.register('register', RegisterViewSet,
                               basename='register')
operations_api_router.register('verify-code', SendSmsVerifyCodeViewSet,
                               basename='verify-code')
operations_api_router.register('login', LoginViewSet,
                               basename='login')

urlpatterns = [
    path('', include((operations_api_router.urls, 'operations'), namespace='operations')),
    # path('login/', obtain_jwt_token, name='login'),
]
