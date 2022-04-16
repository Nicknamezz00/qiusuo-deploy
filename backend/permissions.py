from rest_framework.permissions import BasePermission


class IsManualAuthenticatedOrReadOnly(BasePermission):
    """
    Allows access only to manual authenticated users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_manual_authenticated)