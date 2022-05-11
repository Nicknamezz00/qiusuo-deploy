from django_filters.rest_framework import FilterSet

from users.models import UserInfo


class UserFilter(FilterSet):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'qq', 'email', 'phone']
