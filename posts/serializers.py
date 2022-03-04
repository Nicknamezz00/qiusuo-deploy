from rest_framework import serializers

from posts.models import Post
from users.models import UserInfo


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = '__all__'
