# -*- coding: utf-8 -*-
# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from clothes.models import Brand


# Create your serializers here.
class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
