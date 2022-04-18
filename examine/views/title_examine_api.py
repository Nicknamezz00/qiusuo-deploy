from rest_framework.viewsets import ModelViewSet

from examine.fliter import TitleExaminedFilter
from examine.models import TitleExamine
from examine.serializers import TitleExamineCreateSerializer, TitleExamineDetailSerializer


class TitleExamineViewSet(ModelViewSet):
    queryset = TitleExamine.objects.all()

    # 重写get_serializer_class方法
    def get_serializer_class(self):
        if not self.action == 'create':
            return TitleExamineDetailSerializer
        return TitleExamineCreateSerializer

    ordering_fields = ['created_time', '-is_examined']

    filter_fields = ['owner']
    filter_class = TitleExaminedFilter
