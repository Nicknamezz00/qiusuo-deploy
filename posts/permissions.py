from django.contrib.auth.models import User

from backend.permissions import PerformActionPermission
from posts.models import Post
from users.models import UserInfo


class PostPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """
    def is_author(self, request, view):
        pk = view.kwargs.get('pk')
        obj = None
        if pk:
            obj = Post.objects.get(pk=pk)
            if obj:
                return obj.author.username == request.user.username

        return False

    def has_object_permission(self, request, view, obj):
        assert isinstance(obj, Post)
        if request.user.is_staff:
            return True

        assert isinstance(obj.author, UserInfo)
        assert isinstance(request.user, User)

        return obj.author.user_ptr_id == request.user.id
