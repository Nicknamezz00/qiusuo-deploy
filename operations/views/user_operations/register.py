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
from utils.send_email import send_email


@permission_classes([AllowAny])
class RegisterViewSet(GenericViewSet, CreateModelMixin):
    """手机号 or 邮箱注册"""
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer


@permission_classes([AllowAny])
class SendSmsVerifyCodeViewSet(GenericViewSet, CreateModelMixin):
    """
    发送短信验证码
    """
    serializer_class = SmsVerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #phone = serializer.validated_data["phone"]
        email = serializer.validated_data['email']

        # TODO: third_party = ThirdParty(APIKEY)
        try:
            code = send_email(request, *args, **kwargs)

            code_record = VerifyCode(code=code, email=email)
            code_record.save()

            return Response({
                "success": True,
                "code": 200,
                'msg': '发送成功'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "code": 400,
                'msg': '发送验证码失败',
                'error_msg': e
            }, status=status.HTTP_400_BAD_REQUEST)


        # # TODO: sms_status = third_party.send_sms(code=code, phone=phone)
        # sms_status = 200
        # if sms_status != 200:
        #     return Response({
        #         "success": False,
        #         'msg': '发送验证码失败'
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     code_record = VerifyCode(code=code, phone=phone)
        #     code_record.save()
        #     return Response({
        #         "success": True,
        #         "code": 201,
        #         "msg": '发送成功',
        #         "phone": phone
        #     }, status=status.HTTP_201_CREATED)

