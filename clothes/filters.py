# -*- coding: utf-8 -*-
from django.contrib import admin


class PriceRangeFilter(admin.SimpleListFilter):

    title = 'Intervalo de precio'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('lte50', 'Hasta 50'),
            ('gt50lte100', 'Entre 50 y 100'),
            ('gt100lte250', 'Entre 100 y 250'),
            ('gt250', u'Más de 250'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'lte50':
            return queryset.filter(price__lte=50)
        if self.value() == 'gt50lte100':
            return queryset.filter(price__gt=50, price__lte=100)
        if self.value() == 'gt100lte250':
            return queryset.filter(price__gt=100, price__lte=250)
        if self.value() == 'gt250':
            return queryset.filter(price__gt=250)
