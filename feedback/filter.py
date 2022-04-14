from django_filters import rest_framework as filters

import feedback
from feedback.models import Feedback, FeedbackReply


class FeedbackFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name='author__username',
        lookup_expr='iexact',
    )
    created_at = filters.DateTimeFromToRangeFilter(
        field_name='created_at',
    )
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
    )
    content = filters.CharFilter(
        field_name='content',
        lookup_expr='icontains',
    )

    class Meta:
        model = Feedback
        fields = [
            'author',
            'created_at',
            'title',
            'content',
        ]


class FeedbackReplyFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name='author__username',
        lookup_expr='iexact',
    )
    related_feedback = filters.NumberFilter(
        field_name='related_feedback__id',
        lookup_expr='iexact',
    )
    created_at = filters.DateTimeFromToRangeFilter(
        field_name='created_at',
    )
    content = filters.CharFilter(
        field_name='content',
        lookup_expr='icontains',
    )

    class Meta:
        model = FeedbackReply
        fields = [
            'author',
            'created_at',
            'content',
            'related_feedback'
        ]
