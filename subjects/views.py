from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from subjects.models import Subject
from subjects.serializers import SubjectSerializer


@permission_classes([IsAdminUser])
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('level')
    serializer_class = SubjectSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={
            'success': True,
            'code': 204,
            'msg': '删除成功'
        }, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
