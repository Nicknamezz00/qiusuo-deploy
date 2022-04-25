from rest_framework import serializers

from informations.models import School
from users.models import UserInfo
from .models import TitleExamine


class TitleExamineCreateSerializer(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(
        queryset=School.objects.all(),
        slug_field='school_name',
        required=True)

    class Meta:
        model = TitleExamine
        fields = ['owner', 'title', 'real_name', 'school_id_card', 'school']


class TitleExamineDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        queryset=UserInfo.objects.all(),
        slug_field='id',
        required=False)

    class Meta:
        model = TitleExamine
        fields = ['id', 'owner', 'title', 'real_name', 'school_id_card', 'school', 'is_approved', 'is_rejected', 'reject_reason']
