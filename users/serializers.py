from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from informations.models import School
from informations.serializers import SchoolSerializer
from posts.models import Post
from subjects.models import Subject
from users.models import UserInfo, UserTitle
from examine.models import TitleExamine


class TitleExaminedSetSerializer(serializers.ModelSerializer):
    # add title_examined_set
    def get_queryset(self):
        return TitleExamine.objects.filter(is_approved=True)

    class Meta:
        model = TitleExamine
        fields = [
            'title',
            'real_name',
            'school_id_card',
            'school',
            'is_approved',
            'is_rejected',
            'reject_reason']


class UserProfileSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field='cate_name',
        required=False)
    title_examined_set = TitleExaminedSetSerializer(many=True, read_only=True)
    school = serializers.SlugRelatedField(
        queryset=School.objects.all(),
        slug_field='school_name',
        required=False)

    # def get_area1(self, obj):
    #     area1 = self.initial_data.get('area1')
    #     if not area1:
    #         return None
    #     subject = Subject.objects.get(cate_name=area1)
    #     obj.area1 = subject
    #     obj.save()
    #     return subject.cate_name
    #
    # def get_area2(self, obj):
    #     area2 = self.initial_data.get('area2')
    #     if not area2:
    #         return None
    #     subject = Subject.objects.get(cate_name=area2)
    #     obj.area2 = subject
    #     obj.save()
    #     return subject.cate_name
    #
    # def get_area3(self, obj):
    #     area3 = self.initial_data.get('area3')
    #     if not area3:
    #         return None
    #     subject = Subject.objects.get(cate_name=area3)
    #     obj.area3 = subject
    #     obj.save()
    #     return subject.cate_name

    def create(self, validated_data):
        user = super().create(validated_data)
        user.password = validated_data['password']
        user.save()

        # Add user to default unauthenticated group.
        return user

    def validate(self, attrs):
        raw_password = attrs.get('password')
        if raw_password:
            attrs['password'] = make_password(raw_password)

        return attrs

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)

        school_ser = SchoolSerializer(instance.school)
        res['school'] = school_ser.data

        return res

    class Meta:
        model = UserInfo
        exclude = [
            'password',
            'created_at',
            'groups',
            'user_permissions',
            'is_superuser']


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class UserTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTitle
        fields = '__all__'
