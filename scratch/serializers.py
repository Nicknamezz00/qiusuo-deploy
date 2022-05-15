from rest_framework import serializers

from scratch.models import Scratch


class ScratchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scratch
        fields = '__all__'
