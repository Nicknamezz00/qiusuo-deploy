from rest_framework import viewsets

from informations.models import School
from informations.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
