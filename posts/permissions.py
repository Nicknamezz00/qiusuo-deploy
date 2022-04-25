from django.contrib.auth import get_user

from backend.permissions import PerformActionPermission
from utils.permission_control import get_manual_authentication


class PostPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """

