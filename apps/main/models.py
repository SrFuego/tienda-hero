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
        unique=True,
        verbose_name='Nombre'
    )
    nationality = models.BooleanField(
        verbose_name='Marca nacional'
    )

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

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
        return u'{}'.format(self.name)


def image_path(obj, filename):
    return u'prendas/{}/{}'.format(slugify(obj.name), str(filename))


class Image(models.Model):

    """
    Imágenes de las prendas
    """

    img = StdImageField(
        upload_to=image_path,
        variations={'large': (350, 350), 'thumbnail': (75, 75)},
        verbose_name='Imagen'
    )
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Nombre'
    )

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = u'Imágenes'

    def __unicode__(self):
        return u'{}'.format(self.name)

    def img_thumbnail(self):
        return u'<img src="{}{}" alt="{}">'.format(
            settings.MEDIA_URL, self.img.thumbnail, self.name
        )
    img_thumbnail.allow_tags = True


class Size(models.Model):

    """
    Tallas para las prendas
    """

    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Talla'
    )

    class Meta:
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Cloth(models.Model):

    """
    Prendas
    """

    available = models.BooleanField(
        default=True,
        verbose_name='Disponible'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Marca'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=u'Categoría'
    )
    description = models.TextField(
        blank=True,
        verbose_name=u'Descripción'
    )
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Nombre'
    )
    offer_price = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name='Precio de oferta (opcional)'
    )
    images = models.ManyToManyField(
        Image,
        verbose_name=u'Imágenes de la prenda'
    )
    price = models.PositiveSmallIntegerField(verbose_name='Precio')
    slug = models.SlugField(editable=False, max_length=50)
    size = models.ManyToManyField(
        Size,
        verbose_name='Talla'
    )
    stock = models.PositiveSmallIntegerField(
        verbose_name='Cantidad disponible'
    )

    class Meta:
        verbose_name = 'Prenda'
        verbose_name_plural = 'Prendas'

    def __unicode__(self):
        return u'{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cloth, self).save(*args, **kwargs)
