from backend.permissions import PerformActionPermission


class CommentPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """

    def has_create_permission(self, request, view):
        data = request.data
        request_from = request.user.username
        obj_owner = data.get('author')

        return obj_owner == request_from
