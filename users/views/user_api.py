from django.contrib import auth
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import UserInfo, UserTitle
from users import permissions as user_permissions
from users.serializers import UserTitleSerializer, UserProfileSerializer, ResetPasswordSerializer



class UserInfoViewSet(ModelViewSet):
    """
    需要权限
        1. 'Basic Auth'
        2. JWT认证，请求头Authorization：JWT + 登陆返回的Token
    过滤字段：'id', 'username', 'qq', 'email', 'phone'
    默认排序：'id', 'username', 'created_at' （增序）
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['id', 'username', 'qq', 'email', 'phone']
    ordering_fields = ['id', 'username', 'created_at']

    @action(methods=['GET'], detail=True,
            permission_classes=[permissions.AllowAny])
    def logout(self, request, pk):
        """
        登出
        """
        auth.logout(request)
        return Response(data={
            'success': True,
            'code': 200,
            'msg': '已登出'
        }, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True,
            permission_classes=[permissions.IsAuthenticated])
    def reset_password(self, request, pk):
        """
        修改密码。先发送邮箱验证码。
        """
        instance = self.get_object()
        serializer = ResetPasswordSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(data={
            'success': True,
            'code': 200,
            'msg': '修改密码成功！'
        }, headers=headers, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True,
            permission_classes=[IsAuthenticated])
    def upload_avatar(self, request, pk):
        """
        未实名和实名用户均可以上传头像。
        """
        from utils.upload import upload_avatar
        upload_avatar(request)


class UserTitleViewSet(ModelViewSet):
    """
    用户头衔接口。
    过滤字段：'owner'
    默认排序：'id'（降序），'owner'（增序）
    """
    queryset = UserTitle.objects.all()
    serializer_class = UserTitleSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['owner']

    ordering_fields = ['-id', 'owner']
    # TODO: search
