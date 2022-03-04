from random import choice

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from operations.models import VerifyCode
from operations.serializers import RegisterSerializer, SmsVerifyCodeSerializer
from users.models import UserInfo


@permission_classes([AllowAny])
class RegisterViewSet(GenericViewSet, CreateModelMixin):
    """手机号 or 邮箱注册"""
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer


@permission_classes([AllowAny])
class SendSmsVerifyCodeViewSet(GenericViewSet, CreateModelMixin):
    # 发送短信验证码
    serializer_class = SmsVerifyCodeSerializer

    def generate_code(self):
        """
        生成6位验证码
        """
        seeds = "2351289755"
        random_str = []
        for i in range(6):
            random_str.append(choice(seeds))
        # TODO: return "".join(random_str)
        return "123456"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone"]

        # TODO: third_party = ThirdParty(APIKEY)
        code = self.generate_code()

        # TODO: sms_status = third_party.send_sms(code=code, phone=phone)
        sms_status = 200
        if sms_status != 200:
            return Response({
                'msg': '失败'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, phone=phone)
            code_record.save()
            return Response({
                "code": 201,
                "msg": 'success',
                "phone": phone
            }, status=status.HTTP_201_CREATED)