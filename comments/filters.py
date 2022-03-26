from django_filters.rest_framework import FilterSet

from comments.models import Comment


class CommentFilter(FilterSet):
    class Meta:
        models = Comment
        fields = ['id', 'author', 'post_id']