from django.contrib import auth
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import UserInfo, UserTitle
from users.serializers import UserProfileSerializer


class UserInfoViewSet(ModelViewSet):
    """
    用户接口，目前对于增删改的权限控制不完善！！！
    # TODO: permission control.
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

    @action(methods=['GET'], detail=True)
    def logout(self, request, pk):
        """
        登出，（前端重定向？） 303_SEE_OTHER
        """
        auth.logout(request)
        return Response(data={
            'success': True,
            'code': 303,
            'msg': '已登出'
        }, status=status.HTTP_303_SEE_OTHER)


class UserTitleViewSet(ModelViewSet):
    """
    用户头衔接口。
    过滤字段：'owner'
    默认排序：'id'（降序），'owner'（增序）
    """
    queryset = UserTitle.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['owner']

    ordering_fields = ['-id', 'owner']
    # TODO: search
