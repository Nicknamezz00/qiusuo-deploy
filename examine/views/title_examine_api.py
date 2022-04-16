from rest_framework.response import Response
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

    def post(self, request, *args, **kwargs):
        return super.post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super.get(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super.put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super.patch(request, *args, **kwargs)

    ordering_fields = ['created_time', '-is_examined']

    filter_fields = ['owner']
    filter_class = TitleExaminedFilter

