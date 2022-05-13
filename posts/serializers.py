from rest_framework import serializers

from comments.models import Comment
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

    comment = serializers.SerializerMethodField()

    def get_comment(self, obj):
        comments = Comment.objects.filter(
            post_id=obj.id).values().order_by('-created_at')
        return comments

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)

        author = instance.author
        author_ser = InnerAuthorSerializer(author)
        res['author'] = author_ser.data
        # 一级评论数量
        res['comment_count'] = res.comment.filter(parent=None).count()

        return res

    class Meta:
        model = Post
        depth = 3
        fields = '__all__'
