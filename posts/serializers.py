from collections import OrderedDict

from rest_framework import serializers

from posts.models import Post
from users.models import UserInfo


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=UserInfo.objects.all(), slug_field='id')

    class Meta:
        model = Post
        depth = 1
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        repr_author = OrderedDict()
        repr_author['id'] = instance.author.id
        repr_author['username'] = instance.author.username
        res['author'] = repr_author
        return res
