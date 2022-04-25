from django.contrib.auth import get_user
from rest_framework.permissions import BasePermission

from comments.models import Comment
from users.models import UserInfo
from utils.permission_control import get_manual_authentication

SAFE_ACTIONS = 'list'
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class PerformActionPermission(BasePermission):
    """
    Assume we have already granted permission
    from `IsManualAuthenticatedOrReadOnly` or `IsAuthenticatedOrReadOnly`
    """

    def is_author(self, request, view):
        pk = view.kwargs.get('pk')
        obj = None
        if pk:
            obj = Comment.objects.get(pk=pk)
            return obj.author.username == request.user.username

        return False


    def has_create_permission(self, request, view):
        return self.is_author(request, view)

    def has_retrieve_permission(self, request, view):
        return self.is_author(request, view)

    def has_update_permission(self, request, view):
        return self.is_author(request, view)

    def has_destroy_permission(self, request, view):
        return self.is_author(request, view)

    def has_permission(self, request, view):
        # safe action.
        if view.action == SAFE_ACTIONS or request.method in SAFE_METHODS:
            return True

        # bypass.
        if request.user and (
                request.user.is_staff or request.user.is_superuser):
            return True

        if view.action == 'create':
            return self.has_create_permission(request, view)
        elif view.action == 'retrieve':
            return self.has_retrieve_permission(request, view)
        elif view.action == 'update' or view.action == 'partial_update':
            return self.has_create_permission(request, view)
        elif view.action == 'destroy':
            return self.has_destroy_permission(request, view)
        else:
            raise Exception("omission behavior in `PerformActionPermission`")
