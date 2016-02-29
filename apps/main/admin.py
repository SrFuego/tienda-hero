# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import (
    Brand,
    Category,
    Clothes,
    Image,
)


# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nationality',
    )
    ordering = ('name', 'nationality', )


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
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'img_thumbnail',
    )
