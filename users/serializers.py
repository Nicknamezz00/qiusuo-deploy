from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from examine.models import TitleExamine
from informations.models import School
from informations.serializers import SchoolSerializer
from operations.models import VerifyCode
from subjects.models import Subject
from users.models import UserInfo, UserTitle


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

    def create(self, validated_data):
        user = super().create(validated_data)
        user.password = validated_data['password']
        # TODO: 1. Consider add user to some default unauthenticated group.
        # TODO: 2. Make sure email or phone is unique when
        #          creating user with staff authorization.
        user.save()
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
            'is_superuser'
        ]


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
        label="?????????",
        error_messages={
            "blank": "??????????????????",
            "required": "??????????????????",
            "max_length": "?????????????????????",
            "min_length": "?????????????????????"},
        help_text="?????????")

    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "blank": "??????????????????",
            "required": "?????????????????????",
        }, label='????????????')

    def validate_code(self, code):
        """???????????????"""
        email = self.instance.email
        phone = self.instance.phone

        verify_records = None

        if email:
            verify_records = VerifyCode.objects.filter(
                email=email).order_by('-add_time')

        if phone:
            verify_records = VerifyCode.objects.filter(
                phone=phone).order_by('-add_time')

        if not verify_records:
            raise serializers.ValidationError("???????????????")

        # ?????????????????????????????????
        if verify_records:
            last_record = verify_records[0]  # ????????????
            one_minute_ago = (timezone.now()
                              - timedelta(hours=0, minutes=1, seconds=0))
            # 1??????????????????
            if one_minute_ago > last_record.add_time:
                raise serializers.ValidationError("??????????????????")
            if last_record.code != code:
                raise serializers.ValidationError("??????????????????????????????")

    def update(self, instance, validated_data):
        # ????????????
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
