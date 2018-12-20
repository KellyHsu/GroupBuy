from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from datetime import datetime


class ExpiredListFilter(SimpleListFilter):
    title = _(u'進行中')
    parameter_name = 'expired_time'

    def lookups(self, request, model_admin):
        return (
            ('0', _(u'進行中')),
            ('1', _(u'已結束')),
            ('2', _(u'全部')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(expired_time__gt=datetime.now())
        if self.value() == '1':
            return queryset.filter(expired_time__lt=datetime.now())
        if self.value() == '2':
            return queryset