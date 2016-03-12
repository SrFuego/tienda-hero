# -*- coding: utf-8 -*-
# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from clothes.models import Brand, Category, Cloth, Image, Size


# Create your serializers here.
class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category


class ClothSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cloth


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Image


class SizeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Size
