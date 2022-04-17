from collections import OrderedDict

from rest_framework import serializers

from posts.models import Post
from subjects.models import Subject
from users.models import UserInfo


class InnerAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        exclude = ['password', 'created_at', ]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=UserInfo.objects.all(),
        slug_field='username',
        error_messages={
            "blank": "请输入作者名",
            "required": "请输入作者名"},
        help_text="作者名")
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Subject.objects.all(),
        slug_field='cate_name',
        help_text='学科分类')

    class Meta:
        model = Post
        depth = 3
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        author = instance.author
        author_ser = InnerAuthorSerializer(author)
        res['author'] = author_ser.data
        return res
