
from rest_framework.decorators import permission_classes
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from subjects.models import Subject
from subjects.serializers import SubjectSerializer

"""
def getTree(cates):
    dict = {}
    list = []
    for i in cates:
        dict[i['id']] = i

    for j in cates:
        parent_id = j['parent']

        if not parent_id:
            list.append(j)
        else:
            if 'sub_set' not in dict[parent_id]:
                dict[parent_id]['son'] = []
            dict[parent_id]['son'].append(j)
    return list
"""


@permission_classes([IsAdminUser])
class SubjectViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = Subject.objects.all().order_by('level')
    serializer_class = SubjectSerializer
