# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.apps import apps
from django.db import models


# Third party apps imports


# Local imports


# Create your managers here.
class BrandQuerySet(models.QuerySet):

    def availables(self):
        Cloth = apps.get_model('clothes', 'Cloth')
        return self.filter(
            id__in=Cloth.objects.availables().values_list(
                'brand', flat=True).distinct())

    def nationals(self):
        return self.availables().filter(national=True)

    def internationals(self):
        return self.availables().filter(national=False)


class CategoryQuerySet(models.QuerySet):

    def availables(self):
        Cloth = apps.get_model('clothes', 'Cloth')
        return self.filter(
            id__in=Cloth.objects.availables().values_list(
                'category', flat=True).distinct())


class SizeQuerySet(models.QuerySet):

    def availables(self):
        Cloth = apps.get_model('clothes', 'Cloth')
        return self.filter(
            id__in=Cloth.objects.availables().values_list(
                'size', flat=True).distinct())


class ClothesQuerySet(models.QuerySet):

    def availables(self):
        return self.filter(available=True)

    def for_brand(self, brand):
        return self.availables().filter(brand__name=brand)

    def nationals(self):
        return self.availables().filter(brand__national=True)

    def internationals(self):
        return self.availables().filter(brand__national=False)

    def for_size(self, size):
        return self.availables().filter(size__name=size)
