import json

import requests
from rest_framework import viewsets, status
from rest_framework.response import Response


class SendSmsVerifyCode(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.send_url = 'Currently None'

    def send_verify_code(self, code, phone):
        """
        :param code: 验证码
        :param phone: 手机号
        :return:
        """
        params = {
            "apikey": self.api_key,
            "phone": phone,
            "text": '您的验证码是{code}.'.format(code=code)
        }

        response = requests.post(self.send_url, data=params)
        return json.loads(response)


class MyModelViewSet(viewsets.ModelViewSet):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={
            'success': True,
            'code': 204,
            'msg': '删除成功'
        }, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        data = super().update(request, *args, **kwargs).data
        data['code'] = 200
        data['success'] = True
        return Response(data=data, status=status.HTTP_200_OK)


# TODO: Custom response with api version.
class VersionResponse:
    pass
