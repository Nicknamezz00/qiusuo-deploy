from rest_framework import serializers

from informations.models import School
from users.models import UserInfo
from .models import TitleExamine


class TitleExamineCreateSerializer(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(
        queryset=School.objects.all(),
        slug_field='school_name',
        required=False)

    class Meta:
        model = TitleExamine
        fields = ['owner', 'title', 'real_name', 'school_id_card', 'school']


class TitleExamineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleExamine
        fields = ['id', 'title', 'real_name', 'school_id_card', 'school', 'is_approved', 'is_rejected', 'reject_reason']
