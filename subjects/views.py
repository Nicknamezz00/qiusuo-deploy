from rest_framework.decorators import permission_classes
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from subjects.models import SubjectCategory_1
from subjects.serializers import SubjectSerializer


@permission_classes([IsAdminUser])
class SubjectViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = SubjectCategory_1.objects.all()
    serializer_class = SubjectSerializer
