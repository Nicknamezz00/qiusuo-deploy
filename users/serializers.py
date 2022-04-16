from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from posts.models import Post
from subjects.models import Subject
from users.models import UserInfo, UserTitle
from examine.models import TitleExamine


class InnerPostSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at', 'category', 'status']


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

    # TODO: subject会被覆盖
    # 超级用户手动创建用户
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # Add user to default unauthenticated group.

        return user

    def validate(self, attrs):
        raw_password = attrs['password']
        if raw_password:
            attrs['password'] = make_password(raw_password)
        return attrs

    class Meta:
        model = UserInfo
        fields = '__all__'


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class UserTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTitle
        fields = '__all__'
