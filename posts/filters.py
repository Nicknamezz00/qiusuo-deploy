from django_filters import rest_framework

from posts.models import Post


class PostFilter(rest_framework.FilterSet):
    author = rest_framework.CharFilter(
        field_name='author__username', lookup_expr='iexact')
    title = rest_framework.CharFilter(
        field_name='title', lookup_expr='icontains')
    category = rest_framework.CharFilter(
        field_name='category', lookup_expr='iexact')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category']
