from django.contrib.auth.models import User

from backend.decoraters import pass_safe_method
from backend.permissions import PerformActionPermission
from comments.models import Comment
from users.models import UserInfo


class CommentPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """

    @pass_safe_method
    def is_author(self, request, view, detail=None):
        # Defensive.
        if detail is None:
            raise Exception("Exception in `CommentPermission`")

        if not detail:
            # create action
            author = request.data.get('author')
            return author == request.user.username
        else:
            pk = view.kwargs.get('pk')
            obj = Comment.objects.get(pk=pk)
            return obj.author.username == request.user.username

    def has_object_permission(self, request, view, obj):
        assert isinstance(obj, Comment)
        if request.user.is_staff:
            return True

        assert isinstance(obj.author, UserInfo)
        assert isinstance(request.user, User)

        return obj.author.user_ptr_id == request.user.id

