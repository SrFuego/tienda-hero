# -*- coding: utf-8 -*-
# Python imports


# Django imports


# Third party apps imports
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet


# Local imports
from clothes.models import Brand, Category, Cloth, Image, Size
from .serializers import (
    BrandSerializer, CategorySerializer, ClothSerializer, ImageSerializer,
    SizeSerializer, )


# Create your views here.
class BaseViewSet(ReadOnlyModelViewSet):

    filter_backends = (filters.DjangoFilterBackend, )
    http_method_names = [u'get']


class BrandViewSet(BaseViewSet):

    filter_fields = ('national', )
    queryset = Brand.objects.availables()
    serializer_class = BrandSerializer


class CategoryViewSet(BaseViewSet):

    filter_fields = ('gender', )
    queryset = Category.objects.availables()
    serializer_class = CategorySerializer


class ClothViewSet(BaseViewSet):

    filter_fields = ('brand', 'category', 'size')
    queryset = Cloth.objects.availables()
    serializer_class = ClothSerializer


class ImageViewSet(BaseViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class SizeViewSet(BaseViewSet):

    queryset = Size.objects.availables()
    serializer_class = SizeSerializer
