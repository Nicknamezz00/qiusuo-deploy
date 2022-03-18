from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin

from subjects.models import Subject
from subjects.serializers import SubjectSerializer


class SubjectViewSet(ModelViewSet, ListModelMixin):
    queryset = Subject
    serializer_class = SubjectSerializer
