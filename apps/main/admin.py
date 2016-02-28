# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import (
    Category,
    Clothes,
)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
    )
    ordering = ('name', 'gender',)


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'photo_thumbnail',
    )
