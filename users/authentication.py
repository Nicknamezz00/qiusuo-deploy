from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

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
