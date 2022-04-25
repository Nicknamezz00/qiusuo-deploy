from django.contrib.auth.models import User

from backend.permissions import PerformActionPermission
from comments.models import Comment
from users.models import UserInfo


class CommentPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """
    def has_object_permission(self, request, view, obj):
        assert isinstance(obj, Comment)
        if request.user.is_staff:
            return True
        obj_owner = obj.author

        assert isinstance(obj_owner, UserInfo)
        assert isinstance(request.user, User)

        return obj_owner.user_ptr_id == request.user.id

