# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import (
    Category,
)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
    )
    ordering = ('name', 'gender',)
