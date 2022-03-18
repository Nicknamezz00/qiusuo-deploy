from rest_framework import serializers

from posts.models import Post
from users.models import UserInfo


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
