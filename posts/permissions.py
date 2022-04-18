from backend.permissions import PerformActionPermission
from utils.permission_control import staff


class PostPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """

    def is_author(self, request, view):
        data = request.data
        request_from = request.user.username

        if staff(request_from):
            return True

        obj_owner = data.get('author')
        return obj_owner == request_from

    def has_create_permission(self, request, view):
        return self.is_author(request, view)

    def has_update_permission(self, request, view):
        return self.is_author(request, view)

    def has_destroy_permission(self, request, view):
        return self.is_author(request, view)
