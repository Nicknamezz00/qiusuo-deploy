from django.contrib.auth import get_user
from rest_framework.permissions import BasePermission

from utils.permission_control import get_manual_authentication

SAFE_ACTIONS = 'list'
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class PerformActionPermission(BasePermission):
    """
    Assume we have already granted permission
    from `IsManualAuthenticatedOrReadOnly` or `IsAuthenticatedOrReadOnly`
    """

    def is_author(self, request, view):
        data = request.data
        user = get_user(request)
        obj_owner = data.get('author')
        return obj_owner == user.username

    def has_create_permission(self, request, view):
        user = get_user(request)
        if user.is_anonymous:
            return False
        manual = get_manual_authentication(user)
        return bool(user and
                    user.is_active and
                    user.is_authenticated and manual)

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
        elif view.action == 'update':
            return self.has_update_permission(request, view)
        elif view.action == 'destroy':
            return self.has_destroy_permission(request, view)
        else:
            raise Exception("omission behavior in `PerformActionPermission`")
