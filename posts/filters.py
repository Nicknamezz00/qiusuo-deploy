from django_filters.rest_framework import FilterSet

from posts.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category']
