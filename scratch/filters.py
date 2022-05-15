import django_filters
from django_filters.rest_framework import FilterSet

from scratch.models import Scratch


class ScratchFilter(FilterSet):
    user = django_filters.CharFilter(field_name='user__username')

    class Meta:
        model = Scratch
        exclude = ['content']
