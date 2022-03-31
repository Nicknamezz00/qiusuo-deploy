from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from operations.serializers import LoginSerializer


class LoginViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        res = serializer.context

        # Save Token to database.
        token_db = Token.objects.all()
        return Response(data={
            "success": True,
            "code": 201,
            "msg": '登陆成功',
            "username": res.get('username'),
            "token": res.get('token')
        }, status=status.HTTP_201_CREATED, headers=headers)

