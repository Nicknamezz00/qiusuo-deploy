from rest_framework.permissions import BasePermission

from backend.decoraters import pass_safe_method

SAFE_ACTIONS = 'list'
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class PerformActionPermission(BasePermission):
    """
    Assume we have already granted permission
    from `IsManualAuthenticatedOrReadOnly` or `IsAuthenticatedOrReadOnly`
    """
    def is_author(self, request, view, detail=None):
        pass

    def has_create_permission(self, request, view):
        return self.is_author(request, view, False)

    def has_retrieve_permission(self, request, view):
        return self.is_author(request, view, True)

    def has_update_permission(self, request, view):
        return self.is_author(request, view, True)

    def has_destroy_permission(self, request, view):
        return self.is_author(request, view, True)

    @pass_safe_method
    def has_permission(self, request, view):
        # bypass.
        if request.user and (
                request.user.is_staff or request.user.is_superuser):
            return True

        if view.action == 'create':
            return self.has_create_permission(request, view)
        elif view.action == 'retrieve':
            return self.has_retrieve_permission(request, view)
        elif view.action == 'update' or view.action == 'partial_update':
            return self.has_update_permission(request, view)
        elif view.action == 'destroy':
            return self.has_destroy_permission(request, view)

        # Defensive, this return clause should not make any difference.
        return False

    def has_object_permission(self, request, view, obj):
        pass
