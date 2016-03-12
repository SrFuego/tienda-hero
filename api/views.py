# -*- coding: utf-8 -*-
# Python imports


# Django imports


# Third party apps imports
from rest_framework import viewsets


# Local imports
from clothes.models import Brand
from .serializers import BrandSerializer


# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.availables()
    serializer_class = BrandSerializer
