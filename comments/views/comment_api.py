from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from comments.filters import CommentFilter
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """
    评论接口，需要权限。
        1. 'Basic Auth'
        2. JWT认证，请求头Authorization：JWT + 登陆返回的Token
        
    默认排序字段：'created_at'，最新发布顺序
    过滤字段：'id', 'author', 'post_id'
    后台搜索字段：作者名（author__username），评论贴主键（post_id）
    """
    queryset = Comment.objects.all().order_by('created_at').reverse()
    serializer_class = CommentSerializer

    filter_class = CommentFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    ordering_fields = ['created_at']
    search_fields = ['=author__username', 'post_id']
