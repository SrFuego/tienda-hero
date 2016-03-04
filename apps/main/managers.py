# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.db import models


# Third party apps imports


# Local imports


# Create your managers here.
class ClothesQuerySet(models.QuerySet):

    def available(self):
        return self.filter(available=True)

    def brand(self, brand):
        return self.available().filter(brand__name=brand)

    def national(self):
        return self.available().filter(brand__national=True)

    def international(self):
        return self.available().filter(brand__national=False)

    def size(self, size):
        return self.available().filter(size__name=size)
