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
class Category(models.Model):
    """
    Categoría de las prendas (Jeans, Polos, Camisas, Blusas, etc)
    """

    gender = models.CharField(
                max_length=6,
                choices=GENDER_CHOICES,
                verbose_name='Género'
            )
    name = models.CharField(
                max_length=50,
                verbose_name='Nombre de la Categoría'
            )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        unique_together = ('name', 'gender')

    def __str__(self):
        return '{0}'.format(self.name)


class Clothes(models.Model):
    """
    Prendas
    """

    def image_path(self, filename):
        return 'prendas/{0}/{1}'.format(self.slug, str(filename))

    available = models.BooleanField(default=True)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=50, unique=True)
    offert_price = models.PositiveSmallIntegerField(blank=True, null=True)
    photo = StdImageField(
                upload_to=image_path,
                variations={'large': (640, 480), 'thumbnail': (100, 100)}
            )
    price = models.PositiveSmallIntegerField()
    stock = models.SmallIntegerField()
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'Prenda'
        verbose_name_plural = 'Prendas'

    def __str__(self):
        return '{0}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def photo_thumbnail(self):
        return '<img src="{0}{1}" alt="{2}">'.format(
            settings.MEDIA_URL, self.photo.thumbnail, self.name)

    photo_thumbnail.allow_tags = True
