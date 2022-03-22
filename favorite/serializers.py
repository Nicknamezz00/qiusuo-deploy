from rest_framework import serializers

from favorite.models import UserFavorite, UserFavoriteFolder


class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = '__all__'


class UserFavoriteFoldSerializer(serializers.ModelSerializer):
    favorite_set_bak = UserFavoriteSerializer(many=True, source='favorite_set')

    class Meta:
        model = UserFavoriteFolder
        fields = '__all__'
