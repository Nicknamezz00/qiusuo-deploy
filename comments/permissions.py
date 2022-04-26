from django.contrib.auth.models import User

from backend.permissions import PerformActionPermission
from comments.models import Comment
from users.models import UserInfo


class CommentPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """
    def is_author(self, request, view):
        pk = view.kwargs.get('pk')
        obj = None
        if pk:
            obj = Comment.objects.get(pk=pk)
            if obj:
                return obj.author.username == request.user.username

        return False

    def has_object_permission(self, request, view, obj):
        assert isinstance(obj, Comment)
        if request.user.is_staff:
            return True

        assert isinstance(obj.author, UserInfo)
        assert isinstance(request.user, User)

        return obj.author.user_ptr_id == request.user.id

