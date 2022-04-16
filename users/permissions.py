from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

from users.models import UserInfo

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsManualAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if request.user.is_anonymous:
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated
            )
        else:
            user_info = UserInfo.objects.get(user_ptr_id=request.user.id)
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                user_info.is_manual_authenticated
            )
