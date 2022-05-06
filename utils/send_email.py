import smtplib
from email.mime.text import MIMEText
from random import choice

from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.response import Response

username = r'qiusuo-mc@foxmail.com'
password = 'kqqwciwzuebnciah'


def generate_code():
    """
    生成6位验证码
    """
    seeds = "2351289755"
    random_str = []
    for i in range(6):
        random_str.append(choice(seeds))

    return "".join(random_str)


def get_message(receiver, code):
    content = '''
    <p>邮箱验证码
    <p>尊敬的用户您好！

    <p>您的验证码是：{0}，请在 1 分钟内进行验证。如果该验证码不为您本人申请，请无视。
    <p>官网：<a href="https://qiusuo-mc.cn">qiusuo-mc.cn</a>
'''.format(code)
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = '求索-邮箱验证码'
    msg['From'] = username
    msg['To'] = receiver
    return msg


@require_http_methods(['POST'])
def send_email(request, *args, **kwargs):
    """
    发送邮箱验证码，返回code
    """
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 587)
    try:
        smtp.login(user=username, password=password)
        receiver = request.data['email']
        code = generate_code()
        msg = get_message(receiver, code)
        smtp.sendmail(username, receiver, msg.as_string())
        smtp.quit()
        return code
    except Exception as e:
        smtp.quit()
        return Response({
            "success": False,
            "code": 400,
            'msg': '发送验证码失败',
        }, status=status.HTTP_400_BAD_REQUEST)