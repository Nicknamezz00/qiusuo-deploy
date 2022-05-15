from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter

from backend.helper import MyModelViewSet
from scratch.filters import ScratchFilter
from scratch.models import Scratch
from scratch.permissions import ScratchPermission
from scratch.serializers import ScratchSerializer
from users import permissions as user_permissions


@permission_classes([ScratchPermission,
                     user_permissions.IsManualAuthenticatedOrReadOnly])
class ScratchViewSet(MyModelViewSet):
    queryset = Scratch.objects.all().order_by('-created_at')
    serializer_class = ScratchSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_class = ScratchFilter
