from rest_framework.permissions import BasePermission


SAFE_ACTIONS = 'list'
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class PerformActionPermission(BasePermission):
    """
    Assume we have already granted permission
    from `IsManualAuthenticatedOrReadOnly` or `IsAuthenticatedOrReadOnly`
    """

    def has_create_permission(self, request, view):
        return True

    def has_retrieve_permission(self, request, view):
        return True

    def has_update_permission(self, request, view):
        return True

    def has_destroy_permission(self, request, view):
        return True

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
