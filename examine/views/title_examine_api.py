from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from examine.fliter import TitleExaminedFilter
from examine.models import TitleExamine
from examine.serializers import TitleExamineCreateSerializer, TitleExamineDetailSerializer


class TitleExamineViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = TitleExamine.objects.all().order_by('-created_time')
    permission_classes = [IsAuthenticated]

    # 重写get_serializer_class方法
    def get_serializer_class(self):
        if not self.action == 'create':
            return TitleExamineDetailSerializer
        return TitleExamineCreateSerializer

    def list(self, request, *args, **kwargs):
        """
        此接口仅能获取关于自己的信息
        """
        queryset = self.filter_queryset(self.get_queryset())
        if not request.user.is_superuser:
            queryset = queryset.filter(owner=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['owner']
    filter_class = TitleExaminedFilter
