from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
