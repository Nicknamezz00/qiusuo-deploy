from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from posts.models import Post
from subjects.models import Subject
from users.models import UserInfo, UserTitle


class InnerPostSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at', 'category', 'status']


class UserProfileSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(queryset=Subject.objects.all(), slug_field='cate_name')
    # TODO: subject会被覆盖
    # 超级用户手动创建用户
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserInfo
        fields = [
            'id',
            'username',
            'password',
            'avatar',
            'first_name',
            'last_name',
            'gender',
            'email',
            'qq',
            'phone',
            'intro',
            'created_at',
            'post_set', 'subject']


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class UserTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTitle
        fields = '__all__'
