# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.conf.urls import url


# Third party apps imports
from rest_framework import routers


# Local imports
from .views import (
    BrandViewSet, CategoryViewSet, ClothViewSet, ImageViewSet, SizeViewSet, )


# Create your urls here.
router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'cloth', ClothViewSet)
router.register(r'image', ImageViewSet)
router.register(r'size', SizeViewSet)
