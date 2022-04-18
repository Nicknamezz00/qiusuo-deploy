import logging

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

import utils.upload
from operations.serializers import AvatarUploadSerializer


class AvatarUploadApiViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = AvatarUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = AvatarUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid file'
            })
        else:
            return utils.upload.upload_avatar(request)
