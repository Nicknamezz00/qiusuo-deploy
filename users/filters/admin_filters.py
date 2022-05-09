from datetime import date

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class UserInfoListFilter(admin.SimpleListFilter):
    title = _('user1_info')

    # Query parameter for the filter that will be used in the URL.
    parameter_name = 'use2r_info'


class AdvancedDecadeBornListFilter(UserInfoListFilter):

    def lookups(self, request, model_admin):
        """
        Only show the lookups if there actually is
        anyone born in the corresponding decades.
        """
        qs = model_admin.get_queryset(request)
        if qs.filter(birthday__gte=date(1980, 1, 1),
                     birthday__lte=date(1989, 12, 31)).exists():
            yield ('80s', _('in the eighties'))
        if qs.filter(birthday__gte=date(1990, 1, 1),
                     birthday__lte=date(1999, 12, 31)).exists():
            yield ('90s', _('in the nineties'))
