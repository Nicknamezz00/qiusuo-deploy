from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission

from backend.decoraters import pass_safe_method
from users.models import UserInfo

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsManualAuthenticatedOrReadOnly(BasePermission):
    """
    The request has to be authenticated as a user
    if manual authenticated, the request has permissions to modify database.
    """

    @pass_safe_method
    def has_permission(self, request, view):
        if request.user and (
                request.user.is_staff or request.user.is_superuser):
            return True

        if request.user.is_anonymous:
            return bool(request.method in SAFE_METHODS)
        else:
            user_info = UserInfo.objects.get(user_ptr_id=request.user.id)
            # FIXME: This will be removed later.
            # if user_info.school_id == 2153:
            #     return True
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                user_info.is_manual_authenticated)

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True

        if isinstance(obj, UserInfo):
            return obj.user_ptr_id == user.id
        if isinstance(obj, User):
            return obj.id == user.id

        return user.id == obj.author_id
