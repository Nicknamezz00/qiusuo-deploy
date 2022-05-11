import django_filters
from django_filters.rest_framework import FilterSet

from comments.models import Comment
from subjects.models import Subject


class CommentFilter(FilterSet):
    author = django_filters.CharFilter(
        label='作者',
        field_name='author__username',
        lookup_expr='iexact')
    post_id = django_filters.NumberFilter(
        label='帖子ID', field_name='post_id', lookup_expr='iexact')
    category = django_filters.ModelMultipleChoiceFilter(
        label='学科（按住ctrl多选）',
        field_name='category__cate_name',
        to_field_name='cate_name',
        queryset=Subject.objects.all())
    parent = django_filters.NumberFilter(
        label='父评论ID',
        field_name='parent__id',
        lookup_expr='iexact')

    class Meta:
        models = Comment
        fields = ['id', 'author', 'post_id', 'category', 'parent']
