from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from subjects.models import SubjectCategory_1, SubjectCategory_2, SubjectCategory_3


class SubjectSerializer3(serializers.ModelSerializer):
    class Meta:
        model = SubjectCategory_3
        fields = '__all__'


class SubjectSerializer2(serializers.ModelSerializer):

    class Meta:
        model = SubjectCategory_2
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectCategory_1
        fields = '__all__'
