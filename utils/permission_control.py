from django.contrib.auth.models import User


def staff(obj):
    if isinstance(obj, User) and obj:
        return obj.is_staff or obj.is_superuser

    user = User.objects.filter(username=obj)
    if not user:
        return False
    return bool(user and user.is_staff or user.is_superuser)

