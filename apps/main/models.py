# Python imports


# Django imports
from django.db import models


# Third party apps imports


# Local imports
from .choices import (
    GENDER_CHOICES,
)


# Create your models here.
class Category(models.Model):
    """Categoría de las prendas (Jeans, Polos, Camisas, Blusas, etc)"""

    name = models.CharField(max_length=50,
                            verbose_name='Nombre de la Categoría')
    gender = models.CharField(max_length=6,
                              choices=GENDER_CHOICES,
                              verbose_name='Género')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        unique_together = ('name', 'gender')

    def __str__(self):
        return '{0}'.format(self.name)
