from rest_framework.permissions import BasePermission

from users.models import UserInfo

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsManualAuthenticatedOrReadOnly(BasePermission):
    """
    The request has to be authenticated as a user
    if manual authenticated, the request has permissions to modify database.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user and (
                request.user.is_staff or request.user.is_superuser):
            return True

        if request.user.is_anonymous:
            return bool(request.method in SAFE_METHODS)
        else:
            user_info = UserInfo.objects.get(user_ptr_id=request.user.id)
            # FIXME: this will be removed later.
            # if user_info.school_id == 2153:
            #     return True
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                user_info.is_manual_authenticated)

    def has_object_permission(self, request, view, obj):

        user = request.user
        return user.id == obj.author_id
