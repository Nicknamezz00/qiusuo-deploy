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
        # fields = ['id', 'username', 'password', 'first_name', 'last_name',
        #           'avatar', 'created_at', 'post_count', 'is_login', 'intro',
        #           'is_staff', 'is_superuser']

        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'gender',
            'email',
            'qq',
            'phone',
            'intro',
            'created_at',
            'post_set']


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class UserTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTitle
        fields = '__all__'
