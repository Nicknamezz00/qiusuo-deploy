from rest_framework import serializers

from comments.models import Comment
from users.models import UserInfo


class InnerAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['pk', 'username', 'avatar', 'subject']


class InnerChildSerializer(serializers.ModelSerializer):
    child_comment = serializers.SerializerMethodField(read_only=True)

    def get_child_comment(self, obj):
        all_child_comments = Comment.objects.filter(parent_id=obj.pk)
        child_comments_ser = InnerChildSerializer(
            all_child_comments, many=True)
        return child_comments_ser.data

    class Meta:
        model = Comment
        fields = ['pk', 'author', 'created_at', 'content', 'child_comment']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=UserInfo.objects.all(), slug_field='username')

    parent = serializers.SlugRelatedField(
        required=False,
        queryset=Comment.objects.all(),
        slug_field='id',
        error_messages={
            "blank": "需要父评论pk",
            "required": "需要父评论pk"},
        help_text="父评论pk")

    child_comment = serializers.SerializerMethodField(read_only=True)

    def get_child_comment(self, obj):
        all_child_comments = Comment.objects.filter(parent_id=obj.pk)
        child_comments_ser = InnerChildSerializer(
            all_child_comments, many=True)
        return child_comments_ser.data

    def validate(self, attrs):
        print(attrs)
        return attrs

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        author_ser = InnerAuthorSerializer(instance=instance.author)
        res['author'] = author_ser.data
        return res

    class Meta:
        model = Comment
        depth = 3
        fields = '__all__'
