from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from informations.models import School
from informations.serializers import SchoolSerializer
from operations.models import VerifyCode
from subjects.models import Subject
from users.models import UserInfo, UserTitle
from examine.models import TitleExamine


class TitleExaminedSetSerializer(serializers.ModelSerializer):
    # add title_examined_set
    def get_queryset(self):
        return TitleExamine.objects.filter(is_approved=True)

    class Meta:
        model = TitleExamine
        fields = [
            'title',
            'real_name',
            'school_id_card',
            'school',
            'is_approved',
            'is_rejected',
            'reject_reason']


class UserProfileSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field='cate_name',
        required=False)
    title_examined_set = TitleExaminedSetSerializer(many=True, read_only=True)
    school = serializers.SlugRelatedField(
        queryset=School.objects.all(),
        slug_field='school_name',
        required=False)

    # def get_area1(self, obj):
    #     area1 = self.initial_data.get('area1')
    #     if not area1:
    #         return None
    #     subject = Subject.objects.get(cate_name=area1)
    #     obj.area1 = subject
    #     obj.save()
    #     return subject.cate_name
    #
    # def get_area2(self, obj):
    #     area2 = self.initial_data.get('area2')
    #     if not area2:
    #         return None
    #     subject = Subject.objects.get(cate_name=area2)
    #     obj.area2 = subject
    #     obj.save()
    #     return subject.cate_name
    #
    # def get_area3(self, obj):
    #     area3 = self.initial_data.get('area3')
    #     if not area3:
    #         return None
    #     subject = Subject.objects.get(cate_name=area3)
    #     obj.area3 = subject
    #     obj.save()
    #     return subject.cate_name

    def create(self, validated_data):
        user = super().create(validated_data)
        user.password = validated_data['password']
        user.save()

        # Add user to default unauthenticated group.
        return user

    def validate(self, attrs):
        data = self.context['request'].data
        raw_password = data.get('password')
        if raw_password:
            attrs['password'] = make_password(raw_password)

        return attrs

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)

        school_ser = SchoolSerializer(instance.school)
        res['school'] = school_ser.data

        return res

    class Meta:
        model = UserInfo
        exclude = [
            'password',
            'created_at',
            'groups',
            'user_permissions',
            'is_superuser']


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class UserTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTitle
        fields = '__all__'


class ResetPasswordSerializer(serializers.Serializer):
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

    password = serializers.CharField(
        max_length=12,
        min_length=6,
        write_only=True,
        error_messages={
            "blank": "密码不能为空",
            "required": "请再次输入密码",
        }, label='重置密码')

    def validate_code(self, code):
        """验证码校验"""
        email = self.instance.email
        verify_records = VerifyCode.objects.filter(email=email).order_by("-add_time")

        # 发送时间在一分钟之内的
        if verify_records:
            last_record = verify_records[0]  # 最新一条
            one_minute_ago = (timezone.now()
                              - timedelta(hours=0, minutes=1, seconds=0))
            # 1分钟前发送的
            if one_minute_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误（已接受到）")
            # return code 仅用作验证
        else:
            raise serializers.ValidationError("验证码错误")

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
