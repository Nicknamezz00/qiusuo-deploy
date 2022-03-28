from collections import OrderedDict

from rest_framework import serializers

from comments.models import Comment
from users.models import UserInfo


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=UserInfo.objects.all(), slug_field='id')

    class Meta:
        model = Comment
        depth = 1
        # fields = [
        #     'author',
        #     'post_id', # TODO: detailed serializer
        #     'created_at',
        #     'content',
        #     'category',
        #     'approved']
        fields = '__all__'

#    def get_author(self):

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        repr_author = OrderedDict()
        repr_author['id'] = instance.author.id
        repr_author['username'] = instance.author.username
        res['author'] = repr_author
        return res
