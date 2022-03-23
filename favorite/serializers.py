import os
from collections import OrderedDict
from rest_framework import serializers

from favorite.models import UserFavorite, UserFavoriteFolder
from posts.models import Post

ENV_DEFINE = os.getenv('position')
if ENV_DEFINE == 'online':
    prefix = 'https://qiusuo-1622447-1309638607.ap-shanghai.run.tcloudbase.com/'
else:
    prefix = 'http://127.0.0.1:8000/'

class UserFavoriteSerializer(serializers.ModelSerializer):
    class UserFavoritePostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ['id', 'title', 'content']

        def to_representation(self, instance):
            res = super().to_representation(instance=instance)
            res['url'] = prefix +'post-manage/posts/' +  str(res['id']) + '/'
            del res['id']
            return res

    post = UserFavoritePostSerializer(many=False)

    class Meta:
        model = UserFavorite
        fields = ['post']


class UserFavoriteFoldSerializer(serializers.ModelSerializer):
    favorite_set = UserFavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = UserFavoriteFolder
        fields = ['folder_name', 'favorite_set']
