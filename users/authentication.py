import jwt
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_decode_handler

from users.models import UserInfo


class EmailOrPhoneBackend(ModelBackend):
    """
    自定义用户认证，可使用手机号或邮箱登录
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        :param request:
        :param username: 可以是 `username` `email` `phone`.
        :param password:
        :param kwargs:
        :return:
        """
        try:
            user = User.objects.get(Q(username=username) | Q(phone=username))
            if user.check_password(password):
                return user
        except Exception:
            return None


class JWTAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_Authorization'.upper())
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise AuthenticationFailed('过期了')
        except jwt.DecodeError:
            raise AuthenticationFailed('解码错误')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('不合法的token')

        print(payload)

        user = payload
        return user, token
