# -*- coding: utf-8 -*-
# Python imports


# Django imports
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


# Third party apps imports
from stdimage import StdImageField


# Local imports
from .choices import (
    GENDER_CHOICES,
)

# Create your models here.


class Brand(models.Model):

    """
    Marcas de las prendas
    """

    name = models.CharField(
        max_length=20,
        verbose_name="Nombre de la marca"
    )
    nationality = models.BooleanField(
        verbose_name='Marca nacional'
    )

    def __unicode__(self):
        return u'{}'.format(self.name)


class Category(models.Model):

    """
    Categoría de las prendas (Jeans, Polos, Camisas, Blusas, etc)
    """

    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        verbose_name=u'Género'
    )
    name = models.CharField(
        max_length=50,
        verbose_name=u'Nombre de la Categoría'
    )

    class Meta:
        verbose_name = u'Categoría'
        verbose_name_plural = u'Categorías'
        unique_together = ('name', 'gender')

    def __unicode__(self):
        return '{}'.format(self.name)


def image_path(obj, filename):
    return 'prendas/{}/{}'.format(slugify(obj.name), str(filename))


class Image(models.Model):

    """
    Imágenes de las prendas
    """
    img = StdImageField(
        upload_to=image_path,
        variations={'large': (640, 480), 'thumbnail': (100, 100)}
    )
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'{}'.format(self.name)

    def img_thumbnail(self):
        return '<img src="{}{}" alt="{}">'.format(
            settings.MEDIA_URL, self.img.thumbnail, self.name
        )
    img_thumbnail.allow_tags = True


class Clothes(models.Model):

    """
    Prendas
    """

    available = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=50, unique=True)
    offert_price = models.PositiveSmallIntegerField(blank=True, null=True)
    photo = models.ManyToManyField(Image)
    price = models.PositiveSmallIntegerField()
    slug = models.SlugField(editable=False, max_length=50)
    stock = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Prenda'
        verbose_name_plural = 'Prendas'

    def __unicode__(self):
        return u'{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Clothes, self).save(*args, **kwargs)
