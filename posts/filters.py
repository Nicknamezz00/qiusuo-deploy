import django_filters
from django_filters.rest_framework import FilterSet

from posts.models import Post, ANNOTACION_CHOICE
from subjects.models import Subject


class PostFilter(FilterSet):
    author = django_filters.CharFilter(
        label='作者',
        field_name='author__username', lookup_expr='icontains'
    )
    title = django_filters.CharFilter(
        label='标题',
        field_name='title', lookup_expr='icontains'
    )
    # TODO: When filtering parent subjects filter all their sub
    #  subjects(level >= parent_subject_level).
    category = django_filters.ModelMultipleChoiceFilter(
        label='学科（按住ctrl多选）',
        field_name='category__cate_name',
        to_field_name='cate_name',
        queryset=Subject.objects.all()
    )
    annotation = django_filters.ChoiceFilter(label='标注', choices=ANNOTACION_CHOICE)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category']
