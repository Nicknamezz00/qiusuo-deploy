import json

import requests


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
