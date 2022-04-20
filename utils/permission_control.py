from users.models import UserInfo


def get_manual_authentication(user):
    user_info = UserInfo.objects.get(user_ptr_id=user.id)
    return user_info.is_manual_authenticated
