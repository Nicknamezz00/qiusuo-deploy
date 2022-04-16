from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from examine.models import TitleExamine
from examine.serializers import TitleExamineCreateSerializer, TitleExamineDetailSerializer


class TitleExamineViewSet(ModelViewSet):
    queryset = TitleExamine.objects.all()

    # 重写get_serializer_class方法
    def get_serializer_class(self):
        if self.action == 'list':
            return TitleExamineDetailSerializer
        return TitleExamineCreateSerializer

    ordering_fields = ['created_time', '-is_examined']
