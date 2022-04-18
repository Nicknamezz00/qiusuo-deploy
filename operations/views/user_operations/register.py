from rest_framework.decorators import permission_classes
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from operations.serializers import RegisterSerializer
from users.models import UserInfo


@permission_classes([AllowAny])
class RegisterViewSet(GenericViewSet, CreateModelMixin):
    """手机号 or 邮箱注册"""
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer
