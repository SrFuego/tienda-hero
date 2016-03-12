# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.conf.urls import url


# Third party apps imports


# Local imports
from .views import (
    ClothDetailView, IndexListView, NationalListView, InternationalListView, )

# Create your tests here.


urlpatterns = [
    url(
        r'^national/$',
        NationalListView.as_view(),
        name='national'
    ),
    url(
        r'^international/$',
        InternationalListView.as_view(),
        name='international'
    ),
    url(
        r'^$',
        IndexListView.as_view(),
        name='index'
    ),
    url(
        r'^detail/(?P<slug>[\w-]+)$',
        ClothDetailView.as_view(),
        name='detail'
    ),
]
