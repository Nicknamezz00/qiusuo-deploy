from rest_framework.authtoken.models import Token
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from users.serializers import UserTokenSerializer


class TokenViewSet(GenericViewSet, ListModelMixin):
    queryset = Token.objects.all()
    serializer_class = UserTokenSerializer
