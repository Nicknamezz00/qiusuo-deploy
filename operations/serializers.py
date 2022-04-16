import re
from datetime import datetime, timedelta

from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from backend import constants
from operations.models import VerifyCode
from users.models import UserInfo
from users.serializers import UserProfileSerializer


class RegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        required=True,
        write_only=True,
        max_length=6,
        min_length=6,
        label="验证码",
        error_messages={
            "blank": "请输入验证码",
            "required": "请输入验证码",
            "max_length": "验证码格式错误",
            "min_length": "验证码格式错误"},
        help_text="验证码")

    """手机 or 邮箱注册"""
    password2 = serializers.CharField(
        max_length=12,
        min_length=6,
        write_only=True,
        error_messages={
            "blank": "密码不能为空",
            "required": "请再次输入密码",
        }, label='重置密码')

    def validate_code(self, code):
        """验证码校验"""
        verify_records = VerifyCode.objects.filter(
            phone=self.initial_data["phone"]).order_by("-add_time")

        # 发送时间在一分钟之内的
        if verify_records:
            last_record = verify_records[0]  # 最新一条
            one_minute_ago = (timezone.now()
                              - timedelta(hours=0, minutes=1, seconds=0))
            # 1分钟前发送的
            if one_minute_ago > last_record.add_time:
                raise ValidationError("验证码过期")
            if last_record.code != code:
                raise ValidationError("验证码错误（已接受到）")
            # return code 仅用作验证
        else:
            raise ValidationError("验证码错误")

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']

        if password2 != password:
            raise ValidationError('两次密码不一致，请重新输入！')
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        del validated_data['code']
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'password2', 'phone', 'email',
                  'qq', 'code']


class SmsVerifyCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, required=False)
    email = serializers.EmailField(required=False)

    def validate_phone(self, phone):
        # 手机是否注册
        if UserInfo.objects.filter(phone=phone).count():
            raise ValidationError("用户名已存在")

        # 验证手机号码
        # if not re.match(REGEX_MOBILE, phone):
        #     raise ValidationError("手机号码非法")

        # 验证码发送频率
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1,
                                                     seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago,
                                     phone=phone).count():
            raise ValidationError("距离上一次发送未超过60s")
        return phone

    def validate_email(self, email):
        # email是否注册
        if UserInfo.objects.filter(email=email).count():
            raise ValidationError("用户名已存在")

        # 验证手机号码
        # if not re.match(REGEX_MOBILE, phone):
        #     raise ValidationError("手机号码非法")

        # 验证码发送频率
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1,
                                                     seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago,
                                     email=email).count():
            raise ValidationError("距离上一次发送未超过60s")
        return email


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        error_messages={
            'blank': '请输入手机号/邮箱',
            'required': '请输入手机号/邮箱'
        },help_text='用户名')

    password = serializers.CharField(
        min_length=6,
        max_length=128,
        required=True,
        error_messages={
            'blank': '密码不能为空！',
            'required': '密码不能为空！',
            'min_length': '密码长度至少为6位'
        }, help_text='密码')

    user_info = serializers.SerializerMethodField()

    def get_user_info(self, obj):
        username = obj['username']
        user_ptr_id = User.objects.get(username=username).id
        user_info = UserInfo.objects.get(user_ptr_id=user_ptr_id)
        user_ser = UserProfileSerializer(user_info)
        return user_ser.data

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        # 如果是手机号
        if re.match(constants.REGEX_MOBILE, username):
            # 以手机号登录
            user = UserInfo.objects.filter(phone=username).first()
        elif re.match(constants.REGEX_EMAIL, username):
            # 以邮箱登录
            user = UserInfo.objects.filter(email=username).first()
        else:
            # 以用户名登录
            user = UserInfo.objects.filter(username=username).first()

        if not user:
            raise ValidationError('用户名不存在，用户名一般为手机号/邮箱号')

        attrs['password'] = make_password(password)

        if user and user.check_password(password):
            # 生成token
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            self.context['token'] = token
            self.context['username'] = user.username
            self.context['password'] = user.password
            self.context['user'] = user
            return attrs
        else:
            raise ValidationError('密码错误')

    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'user_info']
