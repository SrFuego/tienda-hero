# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.conf.urls import url


# Third party apps imports
from rest_framework import routers


# Local imports
from .views import BrandViewSet


# Create your urls here.
router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
