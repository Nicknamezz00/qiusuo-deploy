from rest_framework import serializers

from comments.models import Comment
from users import serializers as users_ser
from users.models import UserInfo


class InnerChildSerializer(serializers.ModelSerializer):
    child_comment = serializers.SerializerMethodField(read_only=True)

    def get_child_comment(self, obj):
        all_child_comments = Comment.objects.filter(parent_id=obj.pk)
        child_comments_ser = InnerChildSerializer(
            all_child_comments, many=True)
        return child_comments_ser.data

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        author_ser = users_ser.UserProfileSerializer(instance=instance.author)
        res['author'] = author_ser.data
        return res

    class Meta:
        model = Comment
        fields = '__all__'


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

    def validate_parent(self, parent):
        """如果当前不是一级评论，父评论的id和当前评论所属帖子id是否匹配"""
        init_data = self.initial_data
        post_id: int = int(init_data.get('post_id'))

        if not parent or parent.post_id != post_id:
            raise serializers.ValidationError("post_id与parent不匹配")
        return parent

    def get_child_comment(self, obj):
        all_child_comments = Comment.objects.filter(parent_id=obj.pk)
        child_comments_ser = InnerChildSerializer(
            all_child_comments, many=True)
        return child_comments_ser.data

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        author_ser = users_ser.UserProfileSerializer(instance=instance.author)
        res['author'] = author_ser.data
        return res

    class Meta:
        model = Comment
        depth = 3
        fields = '__all__'
