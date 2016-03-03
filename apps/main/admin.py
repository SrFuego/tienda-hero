# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .filters import PriceRangeFilter

from .models import (
    Brand,
    Category,
    Cloth,
    Image,
    Size,
)


# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'national',
    )
    list_display = (
        'name',
        'national',
    )
    list_filter = ('national', )
    ordering = ('name', )
    search_fields = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'gender',
    )
    list_display = (
        'name',
        'gender',
    )
    list_filter = (
        'gender',
    )
    ordering = ('name', )
    search_fields = ('name', )


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'description',
        'category',
        'brand',
        'stock',
        'images',
        'size',
        'price',
        'offer_price',
        'available',
    )
    list_editable = (
        'available',
    )
    list_display = (
        'name',
        'category',
        'brand',
        'stock',
        'price',
        'offer_price',
        'available',
    )
    list_filter = (
        'category',
        'brand',
        'size',
        PriceRangeFilter,
        'available',
    )
    ordering = (
        'name',
        'category',
        '-stock',
    )
    raw_id_fields = ('images', )
    search_fields = (
        'name',
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'img',
    )
    list_display = (
        'name',
        'img_thumbnail',
    )
    list_per_page = 50
    ordering = ('name', )
    search_fields = ('name', )


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )
    list_display = (
        'name',
    )
    ordering = ('name', )
    search_fields = ('name', )
