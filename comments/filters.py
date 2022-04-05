from django_filters import rest_framework

from comments.models import Comment


class CommentFilter(rest_framework.FilterSet):
    author = rest_framework.CharFilter(
        field_name='author__username', lookup_expr='iexact')
    post_id = rest_framework.NumberFilter(
        field_name='post_id', lookup_expr='iexact')
    category = rest_framework.CharFilter(
        field_name='category', lookup_expr='iexact')
    parent = rest_framework.CharFilter(
        field_name='parent__id', lookup_expr='iexact')

    class Meta:
        models = Comment
        fields = ['id', 'author', 'post_id', 'category', 'parent']
