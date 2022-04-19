from django.contrib.auth import get_user

from backend.permissions import PerformActionPermission


class PostPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """

    def is_author(self, request, view):
        data = request.data

        user = get_user(request)

        if user.is_staff:
            return True

        obj_owner = data.get('author')
        return obj_owner == user.username

    def has_create_permission(self, request, view):
        return self.is_author(request, view)

    def has_update_permission(self, request, view):
        return self.is_author(request, view)

    def has_destroy_permission(self, request, view):
        return self.is_author(request, view)
