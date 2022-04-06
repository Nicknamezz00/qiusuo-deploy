from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from backend import helper
from subjects.models import Subject
from subjects.serializers import SubjectSerializer


@permission_classes([IsAdminUser])
class SubjectViewSet(helper.MyModelViewSet):
    """
    学科分类接口，只有管理员用户才可以调用。
        Basic Auth：管理员账号 + 管理员密码

    默认排序：层级（level）增序（学科涵盖度降序），最高级学科level为0，学科越低层 level越大
    """

    queryset = Subject.objects.all().order_by('level')
    serializer_class = SubjectSerializer
