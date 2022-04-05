from collections import OrderedDict

from rest_framework import serializers

from posts.models import Post
from users.models import UserInfo


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=UserInfo.objects.all(),
        slug_field='username',
        error_messages={
            "blank": "请输入作者名",
            "required": "请输入作者名"},
        help_text="作者名")

    class Meta:
        model = Post
        depth = 1
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        author = instance.author
        author_ser = AuthorSerializer(author)
        res['author'] = author_ser.data
        return res
