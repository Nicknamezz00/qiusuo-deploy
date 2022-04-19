import re

from backend import constants
from users.models import UserInfo


def get_user_by_email_or_phone(username):
    obj = None
    if re.match(constants.REGEX_MOBILE, username):
        obj = UserInfo.objects.get(phone=username)
    elif re.match(constants.REGEX_EMAIL, username):
        obj = UserInfo.objects.get(email=username)
    return obj
