from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from posts.models import Post
from users.models import UserInfo, UserTitle


class InnerPostSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at', 'category', 'status']


class UserProfileSerializer(serializers.ModelSerializer):
    # post_set = InnerPostSetSerializer(many=True)

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
            'post_set']

    # 超级用户手动创建用户
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class UserTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTitle
        fields = '__all__'
