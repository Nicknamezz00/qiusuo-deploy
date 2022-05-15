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
        help_text="作者名"
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Subject.objects.all(),
        slug_field='cate_name',
        help_text='学科分类'
    )
    comment = serializers.SerializerMethodField()
    annotation = serializers.SerializerMethodField()

    class Meta:
        model = Post
        depth = 3
        fields = '__all__'

    def get_comment(self, obj):
        comments = Comment.objects.filter(
            post_id=obj.id).values().order_by('-created_at')
        return comments

    def get_comment_count(self, comments):
        """一级评论数量"""
        cnt = 0
        for comment in comments:
            if not comment['parent_id']:
                cnt += 1
        return cnt

    def get_annotation(self, obj):
        return obj.get_annotation_display()

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        author = instance.author
        author_ser = InnerAuthorSerializer(author)
        res['author'] = author_ser.data
        res['comment_count'] = self.get_comment_count(res.get('comment'))
        return res
