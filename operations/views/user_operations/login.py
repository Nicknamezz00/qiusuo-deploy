from django.contrib import auth
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from operations.serializers import LoginSerializer


@permission_classes([permissions.AllowAny])
class LoginViewSet(GenericViewSet, CreateModelMixin):
    """
    登录接口，登陆成功返回用户相关信息并生成 JWT。
    """
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 不创建用户，只是实现登录逻辑
        user = serializer.context['user']
        auth.login(request=request, user=user)

        headers = self.get_success_headers(serializer.data)
        res = serializer.context

        return Response(data={
            "success": True,
            "code": 201,
            "msg": '登陆成功',
            "username": res.get('username'),
            "token": res.get('token')
        }, status=status.HTTP_201_CREATED, headers=headers)
