from django_filters import rest_framework as filters

from examine.models import TitleExamine


class TitleExaminedFilter(filters.FilterSet):
    owner = filters.CharFilter(field_name='owner__id', lookup_expr='iexact')

    class Meta:
        model = TitleExamine
        fields = ['owner']