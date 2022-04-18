from random import choice

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from operations.models import VerifyCode
from operations.serializers import RegisterSerializer, SmsVerifyCodeSerializer
from users.models import UserInfo
from utils.send_email import send_email


@permission_classes([AllowAny])
class RegisterViewSet(GenericViewSet, CreateModelMixin):
    """手机号 or 邮箱注册"""
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer
