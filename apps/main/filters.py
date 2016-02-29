# -*- coding: utf-8 -*-
from django.contrib import admin


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Intervalo de precio'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('lte50', 'Menor a 50'),
            ('gte50lte100', 'Entre 50 y 100'),
            ('gte100lte250', 'Entre 100 y 250'),
            ('gte250', u'Más de 250'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'lte50':
            return queryset.filter(price__lte=50)
        if self.value() == 'gte50lte100':
            return queryset.filter(price__gte=50, price__lte=100)
        if self.value() == 'gte100lte250':
            return queryset.filter(price__gte=100, price__lte=250)
        if self.value() == 'gte250':
            return queryset.filter(price__gte=250)
