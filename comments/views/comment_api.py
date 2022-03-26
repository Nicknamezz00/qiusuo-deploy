from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from comments.filters import CommentFilter
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at').reverse()
    serializer_class = CommentSerializer

    filter_class = CommentFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    ordering_fields = ['created_at']
    search_fields = ['=author__username', 'post_id']
