from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from backend import helper
from comments.filters import CommentFilter
from comments.models import Comment
from comments.permissions import CommentPermission
from comments.serializers import CommentSerializer
from users import permissions as user_permissions


@permission_classes([CommentPermission,
                     user_permissions.IsManualAuthenticatedOrReadOnly])
class CommentViewSet(helper.MyModelViewSet):
    """
    未实名用户不可以评论。
        1. 'Basic Auth'
        2. JWT认证，请求头Authorization：JWT + 登陆返回的Token
    默认排序字段：'created_at'，最新发布顺序
    过滤字段：'id', 'author', 'post_id', 'category', 'parent'
    后台搜索字段：作者名（=author__username，），评论贴主键（post_id）
    """
    queryset = Comment.objects.all().order_by('created_at').reverse()
    serializer_class = CommentSerializer

    filter_class = CommentFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    ordering_fields = ['created_at']
    search_fields = ['=author__username', 'post_id']

    def update(self, request, *args, **kwargs):
        data = super().update(request, *args, **kwargs).data
        data['code'] = 200
        data['success'] = True
        return Response(data=data, status=status.HTTP_200_OK)
